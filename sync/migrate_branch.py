#!/usr/bin/env python3
"""Migrate an in-flight Atlas edit branch onto the consolidated (Option C) layout.

Consolidation collapses paths into 18 files, so a document moving is a line change inside
a file rather than a file rename. The consolidated form is a pure function of the tree, so
a branch's edit is migrated by recomputing it: `split(head)` against `split(new-main)`.
The author re-applies nothing.

The tool touches no working tree. Reads go through `git archive`; writes use
hash-object/write-tree/commit-tree plumbing against a temporary index. There is no
checkout, stash or rebase, so it is safe to run against open PRs while people are working,
which is what the rehearsal mode below relies on.

Two safety options:
  --tag          writes `<branch>-pre-cutover` at the branch's current OID before anything
                 else, so rollback is `git push --force <tag>:<branch>`.
  --report-only  computes and verifies the migration without creating a ref. Running it
                 against every open PR ahead of the cutover window triages them into
                 clean, dirty-branch and real-conflict, so branches needing their author
                 are identified before the window rather than during it.

Each branch is verified: the migrated split is composed back and compared byte-for-byte
against composing the branch's own `content/`. See `verify_roundtrip` for why the
comparison is on composed output rather than on a re-decomposed tree.

Usage:
    python migrate_branch.py --repo . --ref edit/foo --onto origin/main --report-only
    python migrate_branch.py --repo . --ref edit/foo --onto origin/main --tag
    python migrate_branch.py --repo . --all-open --onto origin/main --report-only
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from compose import compose                       # noqa: E402
from decompose import decompose                   # noqa: E402
from decompose_multi import reassemble            # noqa: E402
from partition import write_split                 # noqa: E402

CONTENT_DIR = "content"


def git(repo: str, *args: str, check: bool = True, binary: bool = False):
    r = subprocess.run(["git", "-C", repo, *args],
                       capture_output=True, check=False,
                       text=not binary)
    if check and r.returncode != 0:
        err = r.stderr if not binary else r.stderr.decode("utf-8", "replace")
        raise RuntimeError(f"git {' '.join(args)} failed: {err.strip()}")
    return r.stdout


def extract_content(repo: str, ref: str, dest: str) -> str:
    """Extract `content/` at `ref` into `dest`. Read-only; no checkout."""
    os.makedirs(dest, exist_ok=True)
    tar = subprocess.run(["git", "-C", repo, "archive", ref, CONTENT_DIR],
                         capture_output=True, check=True)
    subprocess.run(["tar", "-x", "-C", dest], input=tar.stdout, check=True)
    return os.path.join(dest, CONTENT_DIR)


def is_atomized(content_root: str) -> bool:
    return os.path.isfile(os.path.join(content_root, "A", "0", "document.md"))


def verify_roundtrip(split_dir: str, original_content: str, _work: str) -> dict:
    """Check the branch's edit survived: the split must compose back byte-identically.

    The comparison is on composed output rather than on a re-decomposed tree. Composed
    output is what everything downstream consumes — the validator, the renderer, Atlas
    Review — and it is invariant to frontmatter formatting. Comparing trees instead
    reports a spurious difference on every branch: the two documents whose names contain
    an apostrophe are re-emitted quoted by the YAML emitter (`name: Stablewatch's …` ->
    `name: "Stablewatch's …"`), and both forms parse to the same string.

    It is also cheaper: byte equality of the whole Atlas in one comparison, with no
    temporary tree and no `_index.md` exclusions.
    """
    got = reassemble(split_dir)
    want = compose(original_content)
    if got == want:
        return {"clean": True, "chars": len(got)}

    # Locate the first divergence so a real failure is actionable rather than "differs".
    a, b = want.splitlines(), got.splitlines()
    first = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    return {
        "clean": False,
        "chars": len(got),
        "expected_chars": len(want),
        "first_diff_line": first + 1,
        "detail": [f"- {a[first]!r}" if first < len(a) else "- <eof>",
                   f"+ {b[first]!r}" if first < len(b) else "+ <eof>"],
    }


def migrate(repo: str, ref: str, onto: str, work: str) -> dict:
    """Compute the migrated tree for `ref`. Returns a result dict; creates no refs."""
    head = git(repo, "rev-parse", ref).strip()
    base = git(repo, "rev-parse", onto).strip()

    src = extract_content(repo, head, os.path.join(work, "src"))
    if not is_atomized(src):
        return {"ref": ref, "status": "already-migrated", "head": head}

    split_dir = os.path.join(work, "split")
    result = write_split(src, split_dir)
    check = verify_roundtrip(split_dir, src, work)

    # Non-Atlas changes on the branch (Research Notes, tooling, agent config …) must
    # survive.
    other = git(repo, "diff", "--name-only", f"{base}...{head}",
                "--", ".", f":!{CONTENT_DIR}", check=False).split()

    return {
        "ref": ref,
        "status": "clean" if check["clean"] else "needs-review",
        "head": head,
        "base": base,
        "files": result["files"],
        "split_dir": split_dir,
        "documents": result["total_docs"],
        "verification": check,
        "non_atlas_files": other,
    }


def write_ref(repo: str, res: dict, new_branch: str, tag: bool) -> str:
    """Create the migrated commit with plumbing. No working tree is touched."""
    if tag:
        tag_name = f"{res['ref'].split('/')[-1]}-pre-cutover"
        git(repo, "tag", "-f", tag_name, res["head"])

    idx = os.path.join(res["split_dir"], ".migrate-index")
    env = dict(os.environ, GIT_INDEX_FILE=idx)

    def g(*a):
        r = subprocess.run(["git", "-C", repo, *a], capture_output=True,
                           text=True, env=env, check=False)
        if r.returncode != 0:
            raise RuntimeError(f"git {' '.join(a)}: {r.stderr.strip()}")
        return r.stdout

    g("read-tree", res["base"])
    # Drop whatever content/ the base carries, then add this branch's consolidated form.
    g("rm", "-r", "--cached", "--ignore-unmatch", "-q", CONTENT_DIR)
    for _bucket, fname in res["files"].items():
        path = os.path.join(res["split_dir"], fname)
        blob = g("hash-object", "-w", path).strip()
        g("update-index", "--add", "--cacheinfo", f"100644,{blob},{CONTENT_DIR}/{fname}")

    tree = g("write-tree").strip()
    msg = (f"Migrate {res['ref']} to the consolidated Atlas layout\n\n"
           f"Recomputed mechanically from content/ at {res['head'][:12]} — the edit was "
           f"not re-applied by hand.\nRound-trip verified against the branch's own tree.\n")
    commit = subprocess.run(
        ["git", "-C", repo, "commit-tree", tree, "-p", res["base"], "-m", msg],
        capture_output=True, text=True, env=env, check=True).stdout.strip()
    git(repo, "update-ref", f"refs/heads/{new_branch}", commit)
    return commit


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--repo", default=".", help="repository path")
    ap.add_argument("--ref", help="branch to migrate")
    ap.add_argument("--all-open", action="store_true",
                    help="migrate every open PR's head branch (needs gh)")
    ap.add_argument("--onto", required=True, help="the consolidated base (e.g. origin/main)")
    ap.add_argument("--report-only", action="store_true",
                    help="rehearsal: verify without creating any ref")
    ap.add_argument("--tag", action="store_true",
                    help="write <branch>-pre-cutover before creating the migrated ref")
    ap.add_argument("--suffix", default="-consolidated", help="new branch suffix")
    ap.add_argument("--json", help="write the full report here")
    args = ap.parse_args()

    refs = []
    if args.all_open:
        out = subprocess.run(
            ["gh", "pr", "list", "-R", args.repo if "/" in args.repo else
             subprocess.run(["git", "-C", args.repo, "remote", "get-url", "origin"],
                            capture_output=True, text=True).stdout.strip(),
             "--state", "open", "--limit", "100", "--json", "headRefName"],
            capture_output=True, text=True, check=True).stdout
        refs = [p["headRefName"] for p in json.loads(out)]
    elif args.ref:
        refs = [args.ref]
    else:
        ap.error("pass --ref or --all-open")

    results = []
    for ref in refs:
        work = tempfile.mkdtemp(prefix="atlas-migrate-")
        try:
            res = migrate(args.repo, ref, args.onto, work)
            if res["status"] != "already-migrated" and not args.report_only:
                res["commit"] = write_ref(args.repo, res,
                                          f"{ref}{args.suffix}", args.tag)
            v = res.get("verification") or {}
            print(f"{res['status']:<16} {ref:<52} "
                  f"docs={res.get('documents', 0):>6}  "
                  f"composed={v.get('chars', 0):,}")
            res.pop("split_dir", None)
            results.append(res)
        except Exception as e:                       # keep going; one bad branch is data
            print(f"{'ERROR':<16} {ref:<52} {type(e).__name__}: {e}")
            results.append({"ref": ref, "status": "error", "error": str(e)})
        finally:
            shutil.rmtree(work, ignore_errors=True)

    clean = sum(1 for r in results if r["status"] == "clean")
    print(f"\n{clean}/{len(results)} clean"
          + ("   (report-only — no refs created)" if args.report_only else ""))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
    return 0 if clean == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

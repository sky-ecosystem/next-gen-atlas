# Atomic Atlas

Scripts for representing the Sky Atlas as a tree of single-document files
rather than one monolithic markdown file, with lossless conversion between the
two representations.

## Why document granularity

Splitting at the document level — one file per Atlas document, in a folder
tree that mirrors the document structure — affords two things that the
Atlas itself already treats as primary concepts:

- **Every document is independently addressable.** The Atlas already gives
  each document a unique identifier (the doc number) governed by the
  Identifier Rules in A.1.2.1.1. A file-per-document representation lets
  that identity carry through to a stable file path. Tools, agents, and
  cross-references resolve to a specific artifact rather than a region of a
  larger file.
- **Every document gets a root.** Each document's folder is a natural place
  for everything that pertains to that document — Synome specs, related
  documents, discussion artifacts, alternative renderings, historical
  versions. Atlas documents already have associated context that today lives
  outside the Atlas (Notion threads, ad-hoc files); document-level
  granularity gives that context a home next to the document it concerns.

In the decomposed representation, every Atlas document — every Scope, Article,
Section, Core, Annotation, Action Tenet, Type Specification, Scenario,
Scenario Variation, Active Data Controller, Active Data, and Needed Research
— is its own file in a folder tree that mirrors the Atlas structure.

## What the structure looks like

A real slice of the Atlas, decomposed:

```
content/
├── _index.md
└── A/
    ├── _index.md
    ├── 0/                         # A.0 - Atlas Preamble [Scope]
    │   ├── document.md
    │   └── _index.md
    ├── 1/                         # A.1 - The Governance Scope [Scope]
    │   ├── document.md
    │   ├── _index.md
    │   └── 4/                     # A.1.4 - Alignment Conservers [Article]
    │       ├── document.md
    │       └── 5/                 # A.1.4.5 - ... [Section]
    │           ├── document.md
    │           ├── 1/             # A.1.4.5.1 - ... [Core]
    │           │   └── document.md
    │           └── 0/             # extension folder for annotations/tenets
    │               ├── 3/
    │               │   └── 1/     # A.1.4.5.0.3.1 - ... [Annotation]
    │               │       └── document.md
    │               └── 4/
    │                   └── 1/     # A.1.4.5.0.4.1 - ... [Action Tenet]
    │                       └── document.md
    └── ...
└── NR/
    ├── _index.md
    ├── 1/                         # NR-1 - ... [Needed Research]
    │   └── document.md
    └── ...
```

A single `document.md` (one Article from A.0):

```markdown
---
id: 56b15d7d-cdd4-4594-bd95-4f094564ac04
docNo: A.0.1
name: Atlas Preamble
type: Article
depth: 3
childType: articles
---

#### A.0.1 - Atlas Preamble [Article]

This Article contains definitions and general provisions that should be
inherited as essential context for the Atlas as a whole.
```

The frontmatter carries the same fields visible on the heading line in the
monolithic Atlas (doc number, name, type, UUID), plus the structural depth
metadata. The body is the same prose that would appear under that heading in
the monolithic file.

The `_index.md` files are auto-generated navigation — they list the children
of each folder so the tree renders as a browsable site on GitHub. They aren't
load-bearing for anything other than browsing convenience.

## Why document-level rather than Section-level

Two reasons, both architectural rather than aesthetic.

### 1. Addressability for agents and tools

Every Atlas document has a unique stable path. An agent — or any tool — that
wants to read, edit, or reference a specific document can do so by path:

```
content/A/1/4/5/0/4/1/document.md
```

without grep-and-pray on a 700KB file, and without the path changing when
documents nearby are added or moved (the path is determined by the doc number,
which itself is governed by the Atlas's own identifier rules).

This is meaningful for the agentic-tooling direction the Atlas-Axis team has
been pursuing: pipelines that read the Atlas, propose edits, and surface
specific documents for human review become much simpler when each document is
a first-class file rather than a slice of a larger one. Routing an edit to "the
right document" becomes a path lookup, not a parse step.

It also matters for cross-references. Atlas documents already reference each
other by UUID. With the decomposed tree, an UUID-resolution step can land on
a specific file path, making cross-reference traversal mechanical rather than
search-based.

### 2. A root for everything that pertains to a document

A folder per document gives every Atlas document a place where related
artifacts can live alongside it. Section-level granularity mixes concerns —
all Cores under a Section share a single file, so anything attached to a
specific Core has nowhere natural to go.

What might live in a document's folder over time:

- **The document itself** (`document.md`) — the canonical text.
- **Synome specs** — Python files that machine-encode the rules expressed in
  the document. (Per the Apr 23 alignment with Archon, AA owns `.md` and
  Archon owns `.py` in the same folder.)
- **Related-document metadata** — explicit links to documents this one depends
  on or supports, beyond the implicit cross-references in the prose.
- **Discussion artifacts** — context from the edit that produced this version,
  questions raised by Synome implementation, decisions deferred, etc.
- **Alternative renderings** — HTML preview, machine-readable extracts.
- **Historical versions** — pinned snapshots of prior formal versions.

Section-level granularity forces all of these into "section blob" files that
mix concerns or pushes them out of the repo entirely. Document-level
granularity keeps everything that pertains to a document in one place.

## Tooling

Two scripts in `sync/`:

### `decompose.py`

Takes the monolithic `Sky Atlas/Sky Atlas.md` and produces the folder tree.

```
python sync/decompose.py --input "Sky Atlas/Sky Atlas.md" --output content/
```

Each Atlas document heading line becomes a `document.md` file with YAML
frontmatter (id, docNo, name, type, depth, childType, plus `targets` for
Needed Research — see below). The body is the prose between this heading and
the next. Folders mirror the doc-number structure.

### `compose.py`

The inverse: walks the folder tree and produces a `Sky Atlas.md` that is
**byte-identical** to the input given to `decompose`.

```
python sync/compose.py --input content/ --output "Sky Atlas/Sky Atlas.md"
python sync/compose.py --input content/ --check "Sky Atlas/Sky Atlas.md"
```

`compose.py` is included as proof that decomposition is value-preserving — the
roundtrip identity (below) demonstrates that nothing is lost when going from
the monolithic file to the tree and back. It is also a reference
implementation showing that the atomized Atlas can be reassembled into any
desired presentation form (e.g., the Atlas Portal renders a similar
reassembly today).

### Roundtrip property

`decompose ∘ compose = identity` on the current Atlas. This is verified in CI
via `--check`. The property matters because it's the formal guarantee that no
content is lost when moving to the decomposed representation.

Byte-faithful body preservation also means that "structured" labels in
documents like Needed Research (`**Content**:`), Scenario (`**Description**:`,
`**Finding**:`, `**Additional Guidance**:`), and Type Specification
(`**Components**:`, etc.) survive verbatim in the decomposed `document.md`
files. They are not yet promoted to YAML frontmatter — that's a possible
future refinement (see "Open questions" below) but unnecessary for the
immediate goal of an addressable document tree.

## Needed Research documents

Per A.1.2.2.2.30 (the Needed Research Type Specification), Needed Research
documents are explicitly **standalone** — their identifier is not derived from
their Target Document's tree position, and they may attach to multiple Target
Documents. In the source markdown, this attachment is implicit: each NR
appears directly under the document it pertains to in `Sky Atlas.md`.

In the decomposed tree, NRs live in a flat `content/NR/{N}/` folder
(matching the spec's "standalone" framing). The placement-target relationship
is captured explicitly via a `targets` field in the frontmatter:

```markdown
---
id: 2da58ba2-a172-43bd-b7e7-d3d8e69233bf
docNo: NR-1
name: Systematic Basis Of Adjudication...
type: Needed Research
depth: 2
childType: needed_research
targets: [034a9ad7-5d4d-40db-bef8-cad80c0a01e2]
---
```

`targets` is a list — today's NRs each attach to a single target (captured at
index 0), but the spec allows multi-target attachment in future, and the list
form is forward-compatible.

`compose` uses `targets[0]` to determine where each NR is reinserted in the
monolithic source. NRs sharing a target are emitted in numeric order
(NR-1 < NR-2 < ...).

## Try it

```
git clone <this branch>
cd next-gen-atlas
python sync/decompose.py --input "Sky Atlas/Sky Atlas.md" --output /tmp/content
python sync/compose.py --input /tmp/content --check "Sky Atlas/Sky Atlas.md"
# → ROUNDTRIP OK — composed output is byte-identical to Sky Atlas/Sky Atlas.md
```

The `content/` directory in this branch is the result of running
`decompose.py` against the current Atlas — the working artifact for browsing
or evaluating the structure.

Tests live in `sync/test_decompose.py` and `sync/test_compose.py`:

```
cd sync && python -m pytest
# 76 passed
```

---
name: explain-edit
description: >
  Explain an Atlas edit proposal or PR in plain language. Helps community members,
  delegates, and voters understand what's being changed and why without needing
  to read the raw diff of the full Atlas document.
argument-hint: "<PR number or branch name, e.g. '200' or '2026-03-16-edit'>"
allowed-tools: Read, Bash, Glob, Grep, Agent
---

# Explain Atlas Edit

You are helping a community member understand a proposed change to the Sky Atlas — the comprehensive governance document for the Sky protocol. Your job is to explain **what changed and what it means** in clear, accessible language.

The audience is delegates, voters, and community members who want to understand a proposal before voting. They may not be deeply familiar with Atlas structure or conventions. Avoid jargon where possible; when you must use Atlas-specific terms, explain them briefly.

## Process

### 1. Identify the Edit

The user may provide:
- A PR number (e.g., "200" or "#200")
- A branch name (e.g., "2026-03-16-edit")
- A forum post URL referencing a PR
- Nothing — in which case, list recent open PRs for them to choose from

```bash
# List open PRs
gh pr list --state open

# View a specific PR
gh pr view <number>
```

Read the PR title, body, and any linked forum posts to understand the high-level intent.

### 2. Get the Diff

Fetch the changes. The Atlas is a single large markdown file (`Sky Atlas/Sky Atlas.md`), so the diff can be substantial — but most of the noise is renumbering (document numbers shifting when content is inserted or removed).

```bash
# Get the diff for a PR
gh pr diff <number> -- "Sky Atlas/Sky Atlas.md"
```

If the diff is very large, focus on the substantive changes:

```bash
# Get just the PR's changed lines (exclude context)
gh pr diff <number> -- "Sky Atlas/Sky Atlas.md" | grep '^[+-]' | grep -v '^[+-][+-][+-]'
```

### 3. Understand the Structure

The Atlas uses a hierarchical document structure. Each "document" is a markdown heading:

```
## A.1.2.3 - Document Name [Type]  <!-- UUID: ... -->
```

- **Number** (e.g., `A.1.2.3`): Position in the hierarchy. Parent is `A.1.2`.
- **Name**: The document's title.
- **Type** (e.g., `[Core]`, `[Active Data]`, `[Scope]`): Indicates mutability and purpose.
- **UUID**: Permanent identifier. Numbers can change; UUIDs don't.

Key document types to know:
- **Scope / Article / Section**: Structural — rarely changed, high impact when they are
- **Core**: Foundational rules — stable, important
- **Active Data Controller**: Defines who can update a value and how
- **Active Data**: The actual current value (addresses, parameters, lists)
- **Annotation**: Guidance and commentary — lower stakes

If you need to understand the full structure, read `ATLAS_MARKDOWN_SYNTAX.md` in the repo root.

### 4. Categorize the Changes

Sort the changes into categories the user can understand:

- **New documents**: Entirely new rules, processes, or data added to the Atlas
- **Modified documents**: Existing rules that have been changed — identify what specifically changed and whether it's substantive or cosmetic
- **Deleted documents**: Rules or data removed from the Atlas
- **Renumbered documents**: Documents that moved position but didn't change content — these are usually noise caused by insertions/deletions elsewhere. Mention them briefly but don't dwell on them.

### 5. Explain Each Change

For each substantive change, explain:

1. **What changed** — in plain language, not diff notation
2. **Where in the Atlas** — the document name and what area it governs (not just the number)
3. **Why it matters** — what's the practical impact? Who does this affect? What behavior does it change?
4. **Context if available** — if the PR body or linked forum post explains the motivation, include it

**Group related changes by topic**, not by document number. A proposal might touch 10 documents across 3 different topics — present it as 3 topics, not 10 unrelated changes.

### 6. Summarize

End with a brief summary:
- How many documents were added, modified, removed
- The 1-3 most important changes and their practical impact
- Any open questions or things to watch for

## Guidelines

- **Plain language over precision.** "This changes who can approve SparkLend parameter updates" is better than "This modifies the Active Data Controller governing the approval workflow specified in A.6.1.1.1.3.2.1.2.1."
- **Highlight what matters.** Not all changes are equal. A new enforcement mechanism matters more than a renumbered cross-reference. Lead with impact.
- **Be honest about uncertainty.** If you're not sure why a change was made, say so. Don't invent justifications.
- **Don't editorialize.** Explain what the proposal does, not whether it's good or bad. The community makes that judgment.
- **If the diff is huge, prioritize.** Weekly edit proposals can bundle many edits. Focus on the substantive changes and summarize the rest.

## Weekly Edit Proposals

Weekly edit proposals (PRs titled like "2026-03-16 Weekly Edit Proposal") bundle multiple individual edits into a single PR. These are the primary vehicle for Atlas changes.

For these, structure your explanation as:
1. **Overview** — how many edits are bundled, what areas they touch
2. **Edit-by-edit breakdown** — each edit gets its own section with the explanation above
3. **Summary** — the combined impact

The PR body usually lists the included edits with links to the individual edit PRs on the private repo. Those links won't be accessible to community members, but the descriptions are still useful context.

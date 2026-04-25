# Contributing to FLOW SEO

Thank you for considering a contribution. FLOW is a public, evidence-led SEO knowledge base — its value is its discipline. Please read this guide before opening a PR.

## What we accept

- **Source corrections** (highest-priority contribution) — outdated statistics replaced with current cited sources.
- **Net-new docs or prompts** — when they fill a real gap in the F/L/O/W or Local pillars and meet the evidence standard.
- **Editorial improvements** — clearer phrasing, better examples (sourced), corrected typos.
- **Workflow / script improvements** — better CI checks, link validation, evidence linting.
- **Diagram improvements** — clearer visuals, better alt text, accessibility upgrades.

## What we don't accept

- Statistics without a verifiable URL and retrieval date.
- Tactics paraphrased from any single uncited source book.
- Private notes from your own work that haven't been re-derived from public sources.
- Affiliate links or commercial placements presented as neutral recommendations.
- Content that reproduces verbatim from third-party copyrighted material beyond fair-use scope.
- Legacy case studies from the source-influence book — the 17 banned legacy markers are scanned in CI; see `docs/10-references/independence-ledger.md`.

## The evidence standard

Every public statistic in this repo carries:

1. **Year anchor in prose** — "In 2026," / "As of Q1 2026,"
2. **Inline citation** — `(Publisher, *Title*, p. N, YEAR)` or `([Publisher Title](URL), retrieved YYYY-MM-DD)`
3. **Bibliography entry** in `docs/10-references/bibliography.md`
4. **For verified web sources**, also a record in `docs/10-references/stats-provenance.json` with URL, retrieval date, and verified value

Stats without all four elements get rejected at review.

## Banned phrases

The CI checks reject these in any PR diff:

`it's important to note`, `in today's <anything>`, `ever-evolving landscape`, `comprehensive approach`, `holistic strategy`, `leverage` as a noun, `synergy`, `game-changer`, `supercharge`, `unlock the power`, `let's dive in`, `the key to success is`, `as mentioned above`, `world-class`, `cutting-edge`, `next-generation`, `at the end of the day`, `tap into`.

If your prose can survive removing these words, it's stronger without them.

## How to develop locally

1. Clone the repo:
   ```bash
   git clone https://github.com/AgriciDaniel/flow.git
   cd flow
   ```

2. Install Python 3.12+ (only dependency for CI checks):
   ```bash
   python3 --version  # 3.12 or newer
   ```

3. Run the docs check before pushing:
   ```bash
   python3 scripts/check_docs.py
   ```
   Should print `docs check passed`.

4. (Optional) Install markdownlint-cli2 to mirror CI markdown linting locally:
   ```bash
   npm install -g markdownlint-cli2
   markdownlint-cli2 "**/*.md" "!obsidian-vault/**" "!CHANGELOG.md"
   ```

5. (Optional) Test link integrity locally:
   ```bash
   npm install -g markdown-link-check
   find docs -name "*.md" -exec markdown-link-check {} \;
   ```

## Branch + PR workflow

- Fork the repo or create a feature branch named `<type>/<short-slug>` — e.g. `source/aio-click-rate-q2`, `prompt/ecommerce-faq-generator`, `fix/typo-in-flow-framework`.
- Keep PRs focused — one source correction or one new prompt per PR is ideal.
- Reference the relevant issue if applicable.
- The PR template walks through the evidence checklist; complete it before requesting review.

## Prompt files: standard schema

Every prompt in `docs/09-prompts/<stage>/` follows this structure:

```markdown
---
title: "Prompt Title"
description: "One-line description of what the prompt does."
updated: YYYY-MM-DD
tags:
  - prompts
  - <stage>
---

# Prompt Title

## Use This When
One-sentence description of the trigger condition.

## AI Compatibility
Claude, GPT, Gemini, and other long-context models. Note any caveats.

## Inputs
- Bullet list of what the user provides.

## Prompt
\`\`\`text
The actual prompt text the agent receives.
\`\`\`

## Output
- Bullet list of what the agent returns.

## Example
A short worked example.

## See Also
- [[Related FLOW doc]] or relative-path link to a sibling prompt.
```

## Doc files: required sections

Every doc in `docs/` (excluding `docs/09-prompts/` and `docs/10-references/`) follows this structure:

- **Frontmatter** — title, description, updated date, tags
- **Diagram embed** at top (where applicable)
- **`# Doc Title`**
- **`## What This Is`** — what concept the doc covers
- **`## Why It Matters In 2026`** — current evidence with cited stats
- **`## How To Apply`** — actionable bullets, not abstract advice
- **`## AI Agent Prompt`** (where applicable) — fenced ```text``` block an agent can use directly
- **`## Source`** — bullet list of every cited source with URL or PDF page

## Code of Conduct

This project follows the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md). Be respectful, be specific, cite your sources.

## Questions

Open a [Discussion](https://github.com/AgriciDaniel/flow/discussions) for anything that isn't a bug, source correction, or feature request.

Thank you for helping keep FLOW current.

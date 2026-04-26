# FLOW — Claude Code Integration Guide

FLOW is an evidence-led SEO knowledge base designed for direct consumption by AI agents. This file configures how Claude Code and SEO-Agent interact with this repo.

## What This Repo Is

FLOW (Find · Leverage · Optimize · Win) is a four-stage SEO playbook with:
- 72 docs covering the full SEO lifecycle
- 42 AI-ready prompts in `docs/09-prompts/` organized by stage
- 27 diagrams as assets
- `llms.txt` + `llms-full.txt` per the [llmstxt.org](https://llmstxt.org/) spec for agent ingestion
- Every claim anchored to a 2026 source with retrieval date

## Primary AI Consumer: SEO-Agent

[SEO-Agent](https://github.com/AgriciDaniel/claude-seo) ingests this repo into its brain at session start:

```bash
# Mirror docs/ into wiki/flow/ and ingest into brain
python claude-seo/scripts/sync_flow_content.py --source /path/to/flow

# Or ingest directly if already mirrored
python -c "
import sys; sys.path.insert(0, 'claude-seo')
from pathlib import Path
from seo_agent.brain import AgentBrain, ingest_markdown_directory
from seo_agent.core.paths import resolve_paths
paths = resolve_paths()
brain = AgentBrain(paths.brain_dir)
brain.initialize()
count = ingest_markdown_directory(brain, Path('wiki/flow'), source_prefix='flow')
print(f'Ingested {count} files')
"
```

Once ingested, every SEO-Agent REPL session injects relevant FLOW doctrine into the system prompt via `brain.context_block(query)`. You can also query directly:

```
seo-agent> /recall keyword research
```

## Quick Start for Other AI Agents

Point any agent at `llms-full.txt` for one-shot ingestion of the full corpus:

```
# Claude Code / Cursor / Codex / Gemini
Read the file llms-full.txt for complete FLOW doctrine context.
```

Or use `llms.txt` for the short index and fetch individual docs on demand.

## Directory Map

| Path | Contents |
|------|----------|
| `docs/00-START-HERE.md` | Entry point — what FLOW is and how to use it |
| `docs/01-framework/` | FLOW loop, AI search surface map, independence rules |
| `docs/02-foundations/` | Search intent, E-E-A-T, technical + schema foundations |
| `docs/03-find/` | Keyword research, audience avatar, query fan-out |
| `docs/04-leverage/` | Distributed presence, local citations, Reddit/LinkedIn |
| `docs/05-optimize/` | GEO formatting, entity consistency, content CTR |
| `docs/06-win/` | BOFU, dual-surface scorecard, PPC |
| `docs/07-local-seo/` | GBP, local citations, audits, local content |
| `docs/08-playbooks/` | SaaS, e-commerce, service business, B2B, affiliate |
| `docs/09-prompts/` | 42 stage-specific prompts ready for agent invocation |
| `docs/10-references/` | Bibliography, attribution, stats provenance |

## Prompt Library

Prompts in `docs/09-prompts/` follow this pattern:

```
docs/09-prompts/
  find/        ← keyword research, query fan-out, audience avatar prompts
  leverage/    ← citation building, distributed presence prompts
  optimize/    ← entity, GEO, CTR optimization prompts
  win/         ← BOFU, scorecard, measurement prompts
  local/       ← GBP, local audit prompts
```

Each prompt is in a fenced `text` block — copy the content directly into your agent invocation.

## Evidence Standard

All claims in this repo must cite a source with:
- Publication year ≥ 2024
- Retrieval date
- Primary source (no AI-generated stats)

The CI script `scripts/check_docs.py` enforces this on every push. If you add docs, run it first:

```bash
python scripts/check_docs.py
```

## SEO-Agent ↔ FLOW Sync

SEO-Agent mirrors `docs/` into `wiki/flow/` in its own repo. The sync is one-way:

```
FLOW repo docs/ → (sync_flow_content.py) → SEO-Agent wiki/flow/ → (ingest) → brain
```

To update after changes to this repo:

```bash
# From SEO-Agent repo root
python claude-seo/scripts/sync_flow_content.py
```

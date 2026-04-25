# FLOW SEO

> **Find → Leverage → Optimize → Win.**
> An evidence-led SEO knowledge base for humans and AI agents — built for 2026 search reality.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE.md)
[![Made for AI agents](https://img.shields.io/badge/Made_for-AI_agents-purple.svg)](llms.txt)
[![Last updated](https://img.shields.io/badge/Updated-2026--04--25-green.svg)](CHANGELOG.md)

FLOW is a complete operating model for SEO in the AI-search era: classic organic visibility, AI Overviews and LLM citations, local search and Google Business Profile, off-site corroboration, and conversion measurement — all wired together with cited 2026 evidence and 42 standardized AI prompts.

---

## Why FLOW exists

Search in 2026 is not one results page and one click path. The same query can reach a buyer through Google organic, AI Overviews, ChatGPT or Perplexity citations, local pack listings, Reddit threads, YouTube videos, or LinkedIn discussions — often without a single visit to the brand's site. Most public SEO knowledge predates this reality.

FLOW treats those surfaces as one connected system. Every doc here is grounded in a 2026-current source with a retrieval date, every claim that couldn't be verified got dropped, and every prompt is reproducible by an AI agent reading from this repo.

## Who this is for

| If you are… | Start with… |
|---|---|
| **A solo SEO operator or in-house marketer** | [`docs/00-START-HERE.md`](docs/00-START-HERE.md) → [`docs/01-framework/flow-framework.md`](docs/01-framework/flow-framework.md) |
| **A local-business owner or local-SEO consultant** | [`docs/07-local-seo/`](docs/07-local-seo/) — full pillar from map pack to property audits |
| **A B2B / SaaS / service-business strategist** | [`docs/08-playbooks/`](docs/08-playbooks/) — six business-type playbooks |
| **An AI agent** (Claude, GPT, Gemini, Cursor, Codex) | [`llms.txt`](llms.txt) → load context. [`docs/09-prompts/`](docs/09-prompts/) → 42 standardized prompts |
| **An Obsidian power user** | Clone this repo, open [`obsidian-vault/`](obsidian-vault/) as a vault — wikilinks and frontmatter intact |

## Quickstart

### Read on GitHub
1. Open [`docs/00-START-HERE.md`](docs/00-START-HERE.md)
2. Follow the entry-point map for your role
3. Each pillar doc has the same structure: *What this is · Why it matters in 2026 · How to apply · Sources*

### Pair with your AI agent
1. Clone the repo: `git clone https://github.com/AgriciDaniel/flow.git`
2. Point your agent (Claude Code, Cursor, Codex, etc.) at the repo folder
3. Brief it: *"Use FLOW as the framework. Cite the bibliography. No unsourced stats."*
4. Hand it real tasks: draft a brief, audit a page, plan a topic cluster, score a service page on the dual-surface scorecard

### Run as Obsidian vault
1. Clone the repo
2. Open [`obsidian-vault/`](obsidian-vault/) in Obsidian (Open folder as vault)
3. Wikilinks, frontmatter, and the canvas mirror work out of the box

## Repository structure

```
flow/
├── README.md                    ← you are here
├── LICENSE.md                   ← CC BY 4.0 (content) + MIT (scripts)
├── CONTRIBUTING.md              ← how to propose corrections / additions
├── CODE_OF_CONDUCT.md           ← Contributor Covenant 2.1
├── CHANGELOG.md                 ← release history
├── SECURITY.md                  ← vulnerability disclosure policy
├── llms.txt                     ← AI crawler manifest (llmstxt.org spec)
├── llms-full.txt                ← concatenated full-content variant for agent ingestion
├── docs/
│   ├── 00-START-HERE.md
│   ├── 01-framework/            ← FLOW framework, AI search surface map
│   ├── 02-foundations/          ← search intent, E-E-A-T, technical / schema
│   ├── 03-find/                 ← keyword research, audience avatar, query fan-out
│   ├── 04-leverage/             ← distributed presence, citations, Reddit + LinkedIn
│   ├── 05-optimize/             ← GEO formatting, entity consistency, CTR, schema
│   ├── 06-win/                  ← BOFU + conversion, PPC + first-party, scorecard
│   ├── 07-local-seo/            ← Local SEO pillar (map pack, GBP, property audits)
│   ├── 08-playbooks/            ← SaaS / Ecommerce / Service / B2B / Affiliate / Local
│   ├── 09-prompts/              ← 42 standardized AI prompts (find / leverage / optimize / win / local)
│   └── 10-references/           ← bibliography, attribution, independence ledger
├── assets/
│   ├── diagrams/                ← FLOW-native diagrams (PNG)
│   ├── canvases/                ← Obsidian canvas exports
│   └── social-preview.png       ← GitHub social card
├── obsidian-vault/              ← parallel mirror with wikilinks + frontmatter
├── examples/                    ← worked examples per pillar
└── scripts/
    └── check_docs.py            ← evidence-standard CI check
```

## Evidence standard

Every public statistic in this repo carries:

- **Year anchor in prose** ("In 2026," / "As of Q1 2026,")
- **Inline citation** with publisher, title, page or URL
- **Source URL with retrieval date** in the bibliography

Unverifiable stats were dropped. Contradicted stats were replaced with verified alternatives. The full provenance ledger lives at [`docs/10-references/stats-provenance.json`](docs/10-references/stats-provenance.json).

## What this is not

- **Not a replacement for hands-on testing.** Every tactic should be validated against your specific business, audience, and search surfaces.
- **Not a one-time read.** Search shifts faster than annual ebooks can keep up. The bibliography is dated; the framework is not.
- **Not a derivative-work fork** of any single source book. FLOW is independent original work that acknowledges the influence of *Ski Slope Strategy 3.0* by Chris Von Wilpert (Content Mavericks). See [`docs/10-references/attribution.md`](docs/10-references/attribution.md).

## Contributing

Corrections, source improvements, and 2026-current citations are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the evidence standard, prompt schema, and PR checklist.

Found an outdated statistic? Open an issue using the **Source correction** template — it's the highest-value contribution this repo accepts.

## Maintainer

**Daniel Agrici** — built FLOW as a 2026 reframing of decade-old SEO methodology against current AI-search reality. Connect via the repo's Discussions tab.

## License

- **Content** (Markdown, diagrams, prompt text, examples): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code** (scripts, workflows, configs): [MIT](LICENSE.md)
- **Influence acknowledgment**: see [`LICENSE.md`](LICENSE.md) and [`docs/10-references/attribution.md`](docs/10-references/attribution.md)

You can use, adapt, and redistribute the content commercially with attribution. Scripts can be forked without copyleft.

---

*If FLOW helps you ship something, star the repo and share the framework. That's the attribution chain that keeps the evidence layer current.*

# Security Policy

## Supported Versions

This is a documentation repository. "Security" in this context concerns:

- The integrity of the evidence layer (citations, source URLs, retrieval dates)
- The safety of the prompt library when used with AI agents
- The absence of malicious or misleading content in published pages

## Reporting a Vulnerability

If you discover any of the following, please report it:

| Issue type | How to report |
|---|---|
| **Misleading or fabricated citation** in any doc | Open a GitHub issue with the `source-correction` template, or a private maintainer DM if the issue is sensitive |
| **Prompt-injection-prone language** in a `docs/09-prompts/` file (a prompt that could be hijacked when an agent reads it) | Open a private security advisory via GitHub Security tab |
| **Malicious or off-license content** in a contributed PR | Comment on the PR and tag the maintainer; if urgent, use the GitHub Security advisory channel |
| **Vulnerability in `scripts/check_docs.py` or any CI workflow** | Open a private security advisory |

## What we treat as in-scope

- Fabricated statistics presented as verified
- Citation URLs that lead to malicious or unrelated destinations
- Prompts that could exfiltrate user data or perform unsafe actions when run by an AI agent
- Uncredited reproduction of third-party copyrighted content
- License violations in contributed material

## What we do not treat as security issues

- Outdated statistics (these are normal evidence-decay; report via standard `source-correction` issue)
- Stylistic disagreements
- Differences of expert opinion on a tactic's effectiveness
- Reports based on private benchmarks without methodology

## Response timeline

The maintainer aims to acknowledge security reports within 7 days and to publish a fix or response within 30 days for in-scope issues. Public disclosure of a fix happens after the issue is resolved or, in cases of dispute, after a reasonable coordinated-disclosure window.

## Attribution and rightsholders

If you are a publisher, author, or other rightsholder and believe any quoted excerpt or referenced material exceeds fair-use scope, please contact the maintainer directly. The repository will respond promptly with removal, replacement, or further attribution as appropriate.

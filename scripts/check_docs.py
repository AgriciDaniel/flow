#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if str(path.relative_to(ROOT)).startswith("docs/09-prompts/") and path.name != "README.md":
        for header in ["Use This When", "AI Compatibility", "Inputs", "Prompt", "Output", "Example", "See Also"]:
            if f"## {header}" not in text:
                errors.append(f"{path.relative_to(ROOT)} missing prompt header {header}")
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).split("#", 1)[0]
        if not target or re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)} has outside link {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)} broken link {target}")

stats_path = ROOT / "docs" / "10-references" / "stats-provenance.json"
if stats_path.exists():
    data = json.loads(stats_path.read_text(encoding="utf-8"))
    required = {"stat", "found_in", "verified_url", "retrieval_date", "verified_value", "status"}
    for i, item in enumerate(data):
        missing = required - item.keys()
        if missing:
            errors.append(f"stats-provenance record {i} missing {sorted(missing)}")
        if item.get("status") == "verified" and not item.get("verified_url"):
            errors.append(f"stats-provenance record {i} verified without URL")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("docs check passed")

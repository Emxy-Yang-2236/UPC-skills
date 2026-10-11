#!/usr/bin/env python3
"""Create a non-overwriting research workspace. Python standard library only."""

import argparse
import csv
import json
from pathlib import Path
import sys

from _project_schema import TABLES


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--problem", type=Path)
    args = parser.parse_args()
    root = args.project.expanduser().absolute()
    if root.exists() or root.is_symlink():
        parser.error("Target already exists; adapt its files instead of overwriting it.")
    if not args.title.strip():
        parser.error("Title must not be empty.")
    source = args.problem.expanduser().resolve() if args.problem else None
    if source and not source.is_file():
        parser.error("Problem source is not a file.")
    # Read all required inputs before creating the workspace, so a missing
    # packaged asset or unreadable problem does not leave a partial scaffold.
    problem_bytes = source.read_bytes() if source else None
    outline_bytes = (Path(__file__).resolve().parents[1] / "assets/paper-outline.md").read_bytes()
    root.mkdir(parents=True, exist_ok=False)
    for folder in ("src", "data/raw", "data/derived", "figures", "paper"):
        (root / folder).mkdir(parents=True)
    problem_name = "problem" + (source.suffix.lower() or ".txt") if source else "problem.md"
    if source:
        (root / problem_name).write_bytes(problem_bytes)
    else:
        (root / problem_name).write_text("# Problem\n\nPending: provide the complete problem statement.\n", encoding="utf-8")
    if problem_name != "problem.md":
        (root / "problem.md").write_text(f"# Problem source\n\nSee [{problem_name}]({problem_name}).\n", encoding="utf-8")
    (root / "project.json").write_text(json.dumps({
        "format_version": 1, "title": args.title.strip(),
        "stage": "analyze", "paper_path": "paper/manuscript.md",
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for name, fields in TABLES.items():
        with (root / f"{name}.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            if name == "sources" and source:
                writer.writerow({"id": "S0", "kind": "problem", "locator": problem_name, "status": "verified"})
    (root / "research-state.md").write_text(
        "# Research state\n\nStage: problem interpretation.\n\n"
        "Established results: none.\n\nOpen questions: extract requirements and identify missing evidence.\n\n"
        "Next action: read the full problem and choose the first testable model.\n",
        encoding="utf-8",
    )
    (root / "paper/outline.md").write_bytes(outline_bytes)
    print(json.dumps({"created": str(root), "problem": problem_name, "ready": False}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        sys.exit(1)

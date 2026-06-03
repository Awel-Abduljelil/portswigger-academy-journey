#!/usr/bin/env python3
"""Generate a Markdown progress table from a CSV lab log."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_FILE = ROOT / "tracker" / "labs-log.csv"
TRACKER_FILE = ROOT / "tracker" / "labs-tracker.md"


def format_row(row: dict) -> str:
    no = row.get("No", "").strip()
    date = row.get("Date", "").strip()
    topic = row.get("Topic", "").strip()
    title = row.get("Lab Title", "").strip()
    difficulty = row.get("Difficulty", "").strip()
    writeup = row.get("Writeup Link", "").strip() or "N/A"
    return f"| {no} | {date} | {topic} | {title} | {difficulty} | {writeup} |"


def main() -> None:
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Missing CSV input: {CSV_FILE}")

    with CSV_FILE.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    lines = [
        "# PortSwigger Solved Labs Tracker",
        "",
        "This file is generated automatically from `tracker/labs-log.csv` on every commit/push.",
        "",
        "## Solved Labs",
        "",
        "| No | Date | Topic | Lab Title | Difficulty | Writeup Link |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]

    for row in rows:
        lines.append(format_row(row))

    TRACKER_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {TRACKER_FILE} with {len(rows)} rows from {CSV_FILE}")


if __name__ == "__main__":
    main()

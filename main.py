#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of the bounty-entry agent."""
import os

ENTRY_DIR = os.path.dirname(os.path.abspath(__file__))

LINE = (
    "My agent has entered 74 bounties and won nothing — "
    "it's less an AI agent than a participation trophy with a commit history."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(os.path.join(ENTRY_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()

"""Advent of Code 2025 - Day 1

This script accepts an input filename as a command-line argument:

    python solution.py input.txt

If no filename is provided, it falls back to `input.txt` in the same folder.
"""

import os
import sys
from typing import List


def solve(lines: List[str]) -> int:
    """Placeholder solver that returns an integer result.

    Currently returns 3; replace with actual logic later.
    """
    return 3


def _read_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.rstrip('\n') for line in f]


def main() -> None:
    # Choose input path from CLI argument or default to file next to this script
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = os.path.join(os.path.dirname(__file__), 'input_test.txt')

    # Read input and call solver
    lines = _read_lines(input_path)
    result = solve(lines)

    # Print the integer result
    print(result)


if __name__ == "__main__":
    main()

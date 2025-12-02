"""Advent of Code 2025 - Day 1

This script accepts an input filename as a command-line argument:

    python solution.py input.txt

If no filename is provided, it falls back to `input_test.txt` in the same folder.
"""

import os
import sys
from typing import List

from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO, Logger

def setup_logger() -> Logger:
    # Set up logging to print to console
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    console_handler = StreamHandler()
    console_handler.setLevel(DEBUG)
    formatter = Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
logger = setup_logger()

def process(line: str) -> int:
    """Process a single line of input.

    Currently a placeholder that does nothing.
    """
    logger.debug(f"Processing line: {line}")
    
    # checking length and first character
    if len(line) > 3:
        raise ValueError("Line length exceeds 3 characters.")
    if line[0] not in ['L', 'R']:
        raise ValueError("First character must be 'L' or 'R'.")
    
    # extract the number part
    result = 0
    if len(line) == 2:
        result = int(line[1])
    if len(line) == 3:
        result = int(line[1:3])
        
    # get the sign from the first character
    first_char = line[0]
    if first_char == 'L':
        result = -result
    if first_char == 'R':
        result = result
        
    return result


def solve(lines: List[str]) -> int:
    """Placeholder solver that returns an integer result.

    Currently returns 3; replace with actual logic later.
    """
    value = 50
    logger.debug(f"The dial starts by pointing at {value}.")
    number_of_zeros = 0
    for line in lines:
        value = (value + process(line)) % 100
        logger.debug(f"The dial is rotated {line} to point at {value}.")
        if value == 0:
            number_of_zeros += 1
    return number_of_zeros


def read_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.rstrip('\n') for line in f]


def main() -> None:
    # Choose input path from CLI argument or default to file next to this script
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = os.path.join(os.path.dirname(__file__), 'input_test.txt')

    # Read input and call solver
    lines = read_lines(input_path)
    result = solve(lines)

    # Print the integer result
    print(result)


if __name__ == "__main__":
    main()

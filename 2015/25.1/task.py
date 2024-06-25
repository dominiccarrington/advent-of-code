# https://adventofcode.com/2015/day/23
import os
import re
import math
import itertools
from functools import reduce

def sequence_down_col_1(n: int) -> int:
    return int((math.pow(n, 2) - n + 2) / 2)

def sequence_across_row_1(n: int) -> int:
    return int((n * (n + 1)) / 2)

def calculateValue(row: int, column: int) -> int:
    row_start = sequence_down_col_1(row + column - 1)
    iteration = row_start + column - 1

    code = 20151125
    for _ in range(1, iteration):
        code = (code * 252533) % 33554393
    return code

def parseFile(contents: str) -> int:
    matches = re.match(
        r"To continue, please consult the code grid in the manual\.  Enter the code at row (\d+), column (\d+)\.",
        contents
    )

    if matches is None:
        raise ValueError
    
    row = int(matches.group(1))
    column = int(matches.group(2))
    return calculateValue(row, column)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
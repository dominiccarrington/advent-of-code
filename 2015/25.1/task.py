# https://adventofcode.com/2015/day/23
import os
import re
import math
import itertools
from functools import reduce

def sequence(n) -> int:
    return int((math.pow(n, 2) - n + 2) / 2)

def parseFile(contents: str) -> int:
    matches = re.match(
        r"To continue, please consult the code grid in the manual\.  Enter the code at row (\d+), column (\d+).",
        contents
    )

    if matches is None:
        raise ValueError
    row = int(matches.group(1))
    column = int(matches.group(2))
    
    nth_code = sequence(row) + column
    
    code = 20151125
    for _ in range(0, nth_code):
        code = (code * 252533) % 33554393

    return code

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
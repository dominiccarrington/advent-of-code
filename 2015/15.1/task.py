# https://adventofcode.com/2015/day/15
import os
import re
import math
import itertools
from functools import reduce

def parseFile(contents: str) -> int:
    pass

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
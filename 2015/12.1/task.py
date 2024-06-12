# https://adventofcode.com/2015/day/11
import os
import re

def parseFile(pwd: str) -> str:
    matches = re.findall(r"(-?\d+)", pwd)
    return sum([int(m) for m in matches])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
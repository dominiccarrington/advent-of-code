# https://adventofcode.com/2015/day/16
import os
import re
import math

MFCSAM_OUTPUT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def parseLine(line: str) -> tuple[int, bool]:
    matches = re.match(r"Sue (\d+): (.+)$", line)
    if matches is None:
        raise ValueError

    number = int(matches.group(1))
    categories = [c.strip() for c in matches.group(2).split(',')]

    for c in categories:
        m = re.match(r"(\w+): (\d+)", c)
        category_name = m.group(1)
        count = int(m.group(2))

        if MFCSAM_OUTPUT[category_name] != count:
            return (number, False)
    return (number, True)

def parseFile(contents: str) -> int:
    matches = []
    for line in contents.splitlines():
        (sue_no, is_match) = parseLine(line)
        if is_match:
            matches.append(sue_no)
    return matches

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
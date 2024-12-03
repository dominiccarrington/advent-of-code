# https://adventofcode.com/2024/day/3
import os
import re

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def parseLine(line: str) -> int:
    return sum([
        int(m.group(1)) * int(m.group(2))
        for m in pattern.finditer(line)
    ])

def parseFile(fileContents: str) -> int:
    return sum([parseLine(line) for line in fileContents.splitlines()])


def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
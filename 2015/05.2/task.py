# https://adventofcode.com/2015/day/5
import os

def _checkForSingleSpace(line: str):
    for i in range(0, len(line) - 2):
        if line[i] == line[i+2]:
            return True
    return False

def _checkForDuplicate(line: str):
    for i in range(0, len(line) - 4):
        cs = line[i:i+2]
        if line.find(cs, i+2) > -1:
            return True
    return False

def parseLine(line: str):
    return 1 if _checkForSingleSpace(line) and _checkForDuplicate(line) else 0

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(l) for l in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2024/day/2
import os

def parseLine(line: str) -> int:
    levels = [int(x) for x in line.split(' ')]
    isIncreasing = None
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if not (1 <= diff and diff <= 3):
            return False

        if i == 0:
            isIncreasing = levels[0] > levels[1]
        elif isIncreasing and levels[i] < levels[i + 1]:
            return False
        elif not isIncreasing and levels[i] > levels[i + 1]:
            return False
    return True

def parseFile(fileContents: str) -> int:
    safeReports = 0
    for line in fileContents.splitlines():
        safeReports += 1 if parseLine(line) else 0

    return safeReports


def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
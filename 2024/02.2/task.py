# https://adventofcode.com/2024/day/2
import os

def parseLine(line: str) -> int:
    levels = [int(x) for x in line.split(' ')]
    hasFiredDampener = False
    firedDampenerLastTime = False
    increasingConsensus = [
        levels[0] < levels[1],
        levels[1] < levels[2],
        levels[2] < levels[3],
    ]
    isIncreasing = (
        (increasingConsensus[0] and increasingConsensus[1] and not increasingConsensus[2]) or 
        (increasingConsensus[0] and not increasingConsensus[1] and increasingConsensus[2]) or
        (not increasingConsensus[0] and increasingConsensus[1] and increasingConsensus[2]) or
        (increasingConsensus[0] and increasingConsensus[1] and increasingConsensus[2])
    )

    i, j = 0, 1
    while j < len(levels):
        diff = abs(levels[i] - levels[j])
        if not (1 <= diff and diff <= 3):
            if hasFiredDampener:
                return False
            hasFiredDampener = True
            firedDampenerLastTime = True
            j += 1
            continue
        if (isIncreasing and levels[i] > levels[j]) or (not isIncreasing and levels[i] < levels[j]):
            if hasFiredDampener:
                return False
            hasFiredDampener = True
            firedDampenerLastTime = True
            j += 1
            continue
            
        if firedDampenerLastTime:
            firedDampenerLastTime = False
            i += 2
        else:
            i += 1
        j += 1
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
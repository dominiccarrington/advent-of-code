# https://adventofcode.com/2023/day/2
import os

def parseLine(line: str) -> int:
    """
    Return 0 if the game is impossible
    """
    line = line[5:]
    [id, pullsStr] = line.strip().split(':')
    pulls = [s.strip() for s in pullsStr.split(';')]
    minRed = 0
    minGreen = 0
    minBlue = 0
    for pull in pulls:
        marbleTypes = [s.strip() for s in pull.split(',')]
        for type in marbleTypes:
            [count, colour] = type.split()
            count = int(count)
            if colour == "red" and count > minRed:
                minRed = count
            if colour == "green" and count > minGreen:
                minGreen = count
            if colour == "blue" and count > minBlue:
                minBlue = count

    return minRed * minGreen * minBlue

def main():
    dir = os.path.dirname(__file__)
    sigma = 0
    with open(dir + '/input.txt') as f:
        for line in f:
            sigma += parseLine(line)

    print(sigma)

if __name__ == "__main__":
    main();
# https://adventofcode.com/2023/day/2
import os

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def parseLine(line: str) -> int:
    """
    Return 0 if the game is impossible
    """
    line = line[5:]
    [id, pullsStr] = line.strip().split(':')
    pulls = [s.strip() for s in pullsStr.split(';')]
    for pull in pulls:
        marbleTypes = [s.strip() for s in pull.split(',')]
        for type in marbleTypes:
            [count, colour] = type.split()
            if colour == "red" and int(count) > MAX_RED:
                return 0
            if colour == "green" and int(count) > MAX_GREEN:
                return 0
            if colour == "blue" and int(count) > MAX_BLUE:
                return 0

    return int(id)

def main():
    dir = os.path.dirname(__file__)
    sigma = 0
    with open(dir + '/input.txt') as f:
        for line in f:
            sigma += parseLine(line)

    print(sigma)
if __name__ == "__main__":
    main();
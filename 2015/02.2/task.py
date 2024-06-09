# https://adventofcode.com/2015/day/2
import os

def parseLine(line: str) -> int:
    lens = [int(i) for i in line.split("x")]

    [l1, l2, l3] = sorted(lens)

    return (l1 * 2) + (l2 * 2) + (l1 * l2 * l3)

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(line) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
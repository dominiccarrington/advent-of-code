# https://adventofcode.com/2015/day/2
import os

def parseLine(line: str) -> int:
    [l, w, h] = [int(i) for i in line.split("x")]

    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(line) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
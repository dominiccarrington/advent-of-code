# https://adventofcode.com/2015/day/1
import os

def parseFile(file_contents: str) -> int:
    floor = 0
    for i in range(0, len(file_contents)):
        c = file_contents[i]
        floor += {"(": 1, ")": -1}[c]
        if floor < 0:
            return i + 1

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
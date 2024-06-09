# https://adventofcode.com/2015/day/1
import os

def parseFile(file_contents: str) -> int:
    floor = 0
    for c in file_contents:
        floor += 1 if c == "(" else 0

    return floor

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
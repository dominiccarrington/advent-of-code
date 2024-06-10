# https://adventofcode.com/2015/day/8
import os

def parseLine(line: str):
    converted = line.replace("\\", "\\\\")
    converted = converted.replace('"', '\\"')
    converted = f'"{converted}"'
    return len(converted) - len(line)

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(l.strip()) for l in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
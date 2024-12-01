# https://adventofcode.com/2015/day/3
import os

def parseLine(line: str) -> int:
    count = 1
    visited = {}
    visited[0] = {}
    visited[0][0] = True

    x = 0
    y = 0
    for c in line:
        if c == "^":
            x -= 1
        elif c == "v":
            x += 1
        elif c == ">":
            y += 1
        elif c == "<":
            y -= 1
        
        if x not in visited:
            visited[x] = {}
        if y not in visited[x]:
            visited[x][y] = True
            count += 1

    return count

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(line) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2015/day/6
import os
import re
import math

def parseLine(grid, line):
    matches = re.match(r"(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)", line)
    if matches is None:
        raise ValueError(line)
    
    action = matches.group(1)
    
    start_row = int(matches.group(2))
    start_col = int(matches.group(3))

    end_row = int(matches.group(4))
    end_col = int(matches.group(5))
    
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if action == "turn on":
                grid[row][col] += 1
            elif action == "turn off":
                grid[row][col] = max(grid[row][col] - 1, 0)
            elif action == "toggle":
                grid[row][col] += 2

def parseFile(contents: str) -> int:
    grid = [[0 for i in range(0, 1000)] for j in range(0, 1000)]
    for line in contents.splitlines():
        parseLine(grid, line)
    
    return sum([cell for row in grid for cell in row])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
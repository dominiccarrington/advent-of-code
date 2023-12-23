# https://adventofcode.com/2023/day/13
import os
import re

def checkReflection(g, start):
    i = start
    j = start + 1

    while i >= 0 and j < len(g):
        if g[i] != g[j]:
            return False
        i -= 1
        j += 1
    return True

def getReflection(g):
    for i in range(len(g) - 1):
        j = i + 1
        if g[i] == g[j] and checkReflection(g, i):
            return j
        
    return None

def parseGrid(grid: list[str]):
    r = getReflection(grid)
    if r is not None:
        return r * 100
    
    r = getReflection([
        "".join([grid[j][i] for j in range(len(grid))])
        for i in range(len(grid[0]))
    ])
    if r is not None:
        return r

    return 0

def parseFile(lines: str):
    return sum([parseGrid(line.strip().split("\n")) for line in lines.split("\n\n")])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()

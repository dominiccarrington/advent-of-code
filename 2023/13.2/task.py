# https://adventofcode.com/2023/day/13
import os
import re

def hammingDistance(one, two):
    distance = 0
    for i in range(len(one)):
        distance += 1 if one[i] != two[i] else 0

    return distance

def checkReflection(g, start, foundSmudge = False):
    i = start - 1
    j = start + 2

    while i >= 0 and j < len(g):
        if not foundSmudge and hammingDistance(g[i], g[j]) == 1:
            foundSmudge = True
        elif g[i] != g[j]:
            return False
        i -= 1
        j += 1
    return foundSmudge

def getReflection(g):
    for i in range(len(g) - 1):
        j = i + 1
        if hammingDistance(g[i], g[j]) < 2 and checkReflection(g, i, hammingDistance(g[i], g[j]) == 1):
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

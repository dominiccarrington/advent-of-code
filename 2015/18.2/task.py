# https://adventofcode.com/2015/day/18
import os
import re
import math

STEPS = 100

def doTick(configuration: list[str]) -> list[str]:
    newConfiguration = []
    for i in range(0, len(configuration)):
        row = configuration[i]
        newRow = ""
        for j in range(0, len(row)):
            neighbours = []
            if i > 0:
                if j > 0:
                    neighbours.append(configuration[i-1][j-1])
                neighbours.append(configuration[i-1][j])
                if j < len(row) - 1:
                    neighbours.append(configuration[i-1][j+1])
            
            if j > 0:
                neighbours.append(configuration[i][j-1])
            if j < len(row) - 1:
                neighbours.append(configuration[i][j+1])

            if i < len(configuration) - 1:
                if j > 0:
                    neighbours.append(configuration[i+1][j-1])
                neighbours.append(configuration[i+1][j])
                if j < len(row) - 1:
                    neighbours.append(configuration[i+1][j+1])
            
            on_neighbours = len([n for n in neighbours if n == "#"])
            
            if configuration[i][j] == "#" and (on_neighbours == 2 or on_neighbours == 3):
                newRow += "#"
            elif configuration[i][j] == "." and on_neighbours == 3:
                newRow += "#"
            else:
                newRow += "."

        newConfiguration.append(newRow)

    return newConfiguration

def parseFile(contents: str) -> int:
    configuration = contents.splitlines()
    configuration[0] = '#' + configuration[0][1:-1] + '#'
    configuration[len(configuration) - 1] = '#' + configuration[len(configuration) - 1][1:-1] + '#'

    for _ in range(0, STEPS):
        configuration = doTick(configuration)
        configuration[0] = '#' + configuration[0][1:-1] + '#'
        configuration[len(configuration) - 1] = '#' + configuration[len(configuration) - 1][1:-1] + '#'
    
    return sum([1 if c == '#' else 0 for i in range(0, len(configuration)) for c in configuration[i]])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
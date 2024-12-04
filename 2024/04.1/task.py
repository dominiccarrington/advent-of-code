# https://adventofcode.com/2024/day/4
import os

searchForward = "XMAS"
searchBackward = "SAMX"

def look(lines, startI, startJ, string):
    searchMatrix = [(0, 1), (1, -1), (1, 0), (1, 1)]

    def searchAlong(searchDirection):
        i = startI
        j = startJ
        for c in string[:-1]:
            if lines[i][j] == c:
                i += searchDirection[0]
                j += searchDirection[1]
                if i < 0 or i >= len(lines):
                    return False
                if j < 0 or j >= len(lines[0]):
                    return False
            else:
                return False
        return lines[i][j] == string[-1]

    return sum([searchAlong(dir) for dir in searchMatrix])

def parseFile(fileContents: str) -> int:
    count = 0
    lines = fileContents.splitlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == searchForward[0]:
                count += look(lines, i, j, searchForward)
            elif lines[i][j] == searchBackward[0]:
                count += look(lines, i, j, searchBackward)
    return count

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2023/day/14
import os

def pushNorth(lines: list[str]):
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c != "O":
                continue
            row = i
            while row > 0 and lines[row - 1][j] == ".":
                lines[row - 1][j] = "O"
                lines[row][j] = "."
                row -= 1

    return lines

def parseFile(lines: list[str]):
    lines = [list(line.strip()) for line in lines]
    
    lines = pushNorth(lines)
    return sum([len(lines) - i for i in range(len(lines)) for c in lines[i] if c == "O"])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

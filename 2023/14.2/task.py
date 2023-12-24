# https://adventofcode.com/2023/day/14
import os
from tqdm import tqdm

CYCLES = 1_000_000_000

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

def pushSouth(lines: list[str]):
    for i in range(len(lines) - 1, -1, -1):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c != "O":
                continue
            row = i
            while row < len(lines) - 1 and lines[row + 1][j] == ".":
                lines[row + 1][j] = "O"
                lines[row][j] = "."
                row += 1

    return lines

def pushEast(lines: list[str]):
    for i in range(len(lines)):
        for j in range(len(lines[i]) - 1, -1, -1):
            c = lines[i][j]
            if c != "O":
                continue
            col = j
            while col < len(lines) - 1 and lines[i][col + 1] == ".":
                lines[i][col + 1] = "O"
                lines[i][col] = "."
                col += 1

    return lines

def pushWest(lines: list[str]):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c != "O":
                continue
            col = j
            while col > 0 and lines[i][col - 1] == ".":
                lines[i][col - 1] = "O"
                lines[i][col] = "."
                col -= 1

    return lines

def printLines(lines):
    print("\n".join(["".join(a) for a in lines]))
    print("---")

def doCycle(lines):
    # printLines(lines)
    lines = pushNorth(lines)
    # printLines(lines)
    lines = pushWest(lines)
    # printLines(lines)
    lines = pushSouth(lines)
    # printLines(lines)
    lines = pushEast(lines)
    # printLines(lines)
    return lines

def parseFile(lines: list[str]):
    lines = [list(line.strip()) for line in lines]
    
    previous = []
    repeatFoundAt = None
    for i in tqdm(range(CYCLES)):
        lines = doCycle(lines)
        
        oneLine = "_".join(["".join(a) for a in lines])
        if oneLine in previous and repeatFoundAt is None:
            repeatFoundAt = (previous.index(oneLine), i)
            break
        previous.append(oneLine)
    
    if repeatFoundAt is not None:
        (cycleStart, cycleEnd) = repeatFoundAt
        cycle = previous[cycleStart:cycleEnd]
        print(cycle[0] == oneLine)

        lines = cycle[(CYCLES - cycleStart - 1) % len(cycle)].split("_")

    return sum([len(lines) - i for i in range(len(lines)) for c in lines[i] if c == "O"])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

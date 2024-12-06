# https://adventofcode.com/2024/day/6
import os

guardChars = ['^', '>', 'v', '<']
guardDirections = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def findGuard(lines: list[str]):
    guard = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in guardChars:
                guard = (y, x, guardChars.index(char))
    
    if guard is None:
        raise ValueError

    return guard

def parseFile(fileContents: str) -> int:
    lines = fileContents.splitlines()
    guard = findGuard(lines)

    guardPos = set([(guard[0], guard[1])])
    while True:
        (i, j, dir) = guard
        modifier = guardDirections[dir]
        newGuardPos = (i + modifier[0], j + modifier[1])
        if not (0 <= newGuardPos[0] and newGuardPos[0] < len(lines) and 0 <= newGuardPos[1] and newGuardPos[1] < len(lines[0])):
            break
        elif lines[newGuardPos[0]][newGuardPos[1]] == '#':
            guard = (guard[0], guard[1], 0 if dir == 3 else dir + 1)
        else:
            guardPos.add(newGuardPos)
            guard = newGuardPos + (dir,)
    return len(guardPos)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
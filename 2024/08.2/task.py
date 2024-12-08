# https://adventofcode.com/2024/day/8
import os
from timeit import timeit

def parseFile(fileContents: str) -> int:
    lines = fileContents.splitlines()
    antinodes = set()
    antenna: dict[str, list[(int, int)]] = {}

    def addAntinode(pos):
        if not (0 <= pos[0] and pos[0] < len(lines)):
            # print('reject', pos)
            return False
        if not (0 <= pos[1] and pos[1] < len(lines[0])):
            # print('reject', pos)
            return False
    
        # print('allow', pos)
        antinodes.add(pos)
        return True

    def printMap():
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                print('#' if (i, j) in antinodes else c, end='')
            print()

    for i, line in enumerate(lines):
        for j in range(len(line)):
            if lines[i][j] == '.':
                continue
            freq = lines[i][j]
            if freq in antenna:
                antenna[freq].append((i, j))
            else:
                antenna[freq] = [(i, j)]

    for locs in antenna.values():
        if len(locs) > 1:
            for loc in locs:
                antinodes.add(loc)
        for i in range(len(locs) - 1):
            for j in range(i + 1, len(locs)):
                locI = locs[i]
                locJ = locs[j]

                diff = (locI[0] - locJ[0], locI[1] - locJ[1])

                currentLocation = locJ
                while addAntinode(currentLocation := (currentLocation[0] - diff[0], currentLocation[1] - diff[1])):
                    pass
                
                currentLocation = locI
                while addAntinode(currentLocation := (currentLocation[0] + diff[0], currentLocation[1] + diff[1])):
                    pass                
    # printMap()
    # print(antinodes)
    return len(antinodes)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    time = timeit(main, 'gc.enable()', number=1)
    print(f"Time Taken: {time} secs")
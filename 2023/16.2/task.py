# https://adventofcode.com/2023/day/14
import os

def parseFileInstance(file, start):
    locationsToCheck = [start]
    locationsAccessed = set()

    while len(locationsToCheck):
        location = locationsToCheck.pop()
        (currentPos, direction) = location
        if currentPos[0] < 0 or currentPos[1] < 0 or currentPos[0] >= len(file) or currentPos[1] >= len(file[0]):
            continue

        if location in locationsAccessed:
            continue

        tile = file[currentPos[0]][currentPos[1]]

        isGoingVertical = abs(direction[0]) == 1
        isGoingHorizontal = abs(direction[1]) == 1

        if tile == "." or (isGoingHorizontal and tile == "-") or (isGoingVertical and tile == "|"):
            newPos = (
                currentPos[0] + direction[0],
                currentPos[1] + direction[1],
            )
            locationsToCheck.append((newPos, direction))
        elif isGoingHorizontal and tile == "|":
            newLocations = [
                ((currentPos[0] - 1, currentPos[1]), (-1, 0)),
                ((currentPos[0] + 1, currentPos[1]), (1, 0)),
            ]
            locationsToCheck.extend([location for location in newLocations if location not in locationsAccessed])
        elif isGoingVertical and tile == "-":
            newLocations = [
                ((currentPos[0], currentPos[1] - 1), (0, -1)),
                ((currentPos[0], currentPos[1] + 1), (0, 1)),
            ]
            locationsToCheck.extend([location for location in newLocations if location not in locationsAccessed])
        elif tile == "/":
            newDirection = (-direction[1], -direction[0])
            newPos = (
                currentPos[0] + newDirection[0],
                currentPos[1] + newDirection[1],
            )
            locationsToCheck.append((newPos, newDirection))
        elif tile == "\\":
            newDirection = (direction[1], direction[0])
            newPos = (
                currentPos[0] + newDirection[0],
                currentPos[1] + newDirection[1],
            )
            locationsToCheck.append((newPos, newDirection))
        locationsAccessed.add(location)
    return len(set([l for (l, d) in locationsAccessed]))

def parseFile(file):
    startingLocations = []
    startingLocations.extend([((i, 0), (0, 1)) for i in range(len(file))])
    startingLocations.extend([((i, len(file[0]) - 1), (0, -1)) for i in range(len(file))])
    startingLocations.extend([((0, i), (1, 0)) for i in range(len(file[0]))])
    startingLocations.extend([((len(file) - 1, i), (-1, 0)) for i in range(len(file[0]))])

    return max([parseFileInstance(file, location) for location in startingLocations])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile([
            [c for c in line.strip()] for line in f.readlines()
        ]))

if __name__ == "__main__":
    main()

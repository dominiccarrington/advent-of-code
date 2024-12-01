# https://adventofcode.com/2023/day/11
import os

def parseFile(lines: list[str]):
    lines = [line.strip() for line in lines]
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            coords = (i, j)
            if lines[i][j] == '#':
                galaxies.append(coords)
    
    emptyRows = []
    emptyCols = []

    for i in range(len(lines)):
        line = lines[i]
        if all([l == "." for l in line]):
            emptyRows.append(i)

    for i in range(len(lines[0])):
        if all([line[i] == '.' for line in lines]):
            emptyCols.append(i)

    actualLocationsForGalaxies = []
    for galaxy in galaxies:
        emptyRowsAbove = len([row for row in emptyRows if row < galaxy[0]])
        emptyColsToLeft = len([col for col in emptyCols if col < galaxy[1]])
        actualLocationsForGalaxies.append((
            galaxy[0] + (emptyRowsAbove * 999_999),
            galaxy[1] + (emptyColsToLeft * 999_999),
        ))

    noOfGalaxies = len(actualLocationsForGalaxies)
    sigma = 0
    for i in range(noOfGalaxies):
        fromGalaxy = actualLocationsForGalaxies[i]

        for j in range(i+1, noOfGalaxies):
            toGalaxy = actualLocationsForGalaxies[j]
            sigma += abs(fromGalaxy[0] - toGalaxy[0]) + abs(fromGalaxy[1] - toGalaxy[1])

    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

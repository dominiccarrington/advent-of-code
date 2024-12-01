# https://adventofcode.com/2023/day/11
import os

def expandUniverse(lines: list[str]):
    newLines = []
    for line in lines:
        newLines.append(line)
        if all([c == '.' for c in line]):
            newLines.append(line)
    
    newUniverse = list([[] for _ in newLines])
    columns = len(newLines[0]) # Square Input
    for i in range(columns):
        for j in range(len(newLines)):
            newUniverse[j].append(newLines[j][i])

        if all(line[i] == '.' for line in newLines):
            for j in range(len(newLines)):
                newUniverse[j].append(newLines[j][i])

    return newUniverse

def parseFile(lines: list[str]):
    universe = expandUniverse(list([l.strip() for l in lines]))

    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            coords = (i, j)
            if universe[i][j] == '#':
                galaxies.append(coords)
    
    noOfGalaxies = len(galaxies)
    sigma = 0
    for i in range(noOfGalaxies):
        fromGalaxy = galaxies[i]

        for j in range(i+1, noOfGalaxies):
            toGalaxy = galaxies[j]
            sigma += abs(fromGalaxy[0] - toGalaxy[0]) + abs(fromGalaxy[1] - toGalaxy[1])

    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

# https://adventofcode.com/2023/day/11
import os
import networkx
from tqdm import tqdm

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

    graph = networkx.Graph()

    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            coords = (i, j)
            if universe[i][j] == '#':
                galaxies.append(coords)
            
            neighbours = []
            if coords[0] > 0:
                neighbours.append((coords[0] - 1, coords[1]))
            if coords[1] > 0:
                neighbours.append((coords[0], coords[1] - 1))
            if coords[0] < len(universe) - 1:
                neighbours.append((coords[0] + 1, coords[1]))
            if coords[1] < len(universe[i]) - 1:
                neighbours.append((coords[0], coords[1] + 1))

            graph.add_edges_from([(coords, n) for n in neighbours])

    sigma = 0
    for i, j in tqdm([(i, j) for j in range(i+1, len(galaxies)) for i in range(len(galaxies)) ]):
        sigma += networkx.dijkstra_path_length(graph, galaxies[i], galaxies[j], lambda _1,_2,_3: 1)

    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

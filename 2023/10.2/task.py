# https://adventofcode.com/2023/day/10
import os
from tqdm import tqdm

TILES = ["|", "-", "L", "J", "7", "F"]

def tilePoints(tile: str, location: (int, int)):
    if tile == "|":
        return [(location[0] + 1, location[1]), (location[0] - 1, location[1])]
    if tile == "-":
        return [(location[0], location[1] + 1), (location[0], location[1] - 1)]
    if tile == "L":
        return [(location[0] - 1, location[1]), (location[0], location[1] + 1)]
    if tile == "J":
        return [(location[0] - 1, location[1]), (location[0], location[1] - 1)]
    if tile == "7":
        return [(location[0] + 1, location[1]), (location[0], location[1] - 1)]
    if tile == "F":
        return [(location[0] + 1, location[1]), (location[0], location[1] + 1)]
    return []

def pointsInto(tile: str, location: (int, int), query: (int, int)):
    return query in tilePoints(tile, location)

def parseFile(lines: list[str]):
    lines = [line.strip() for line in lines]
    
    # Step 1, find starting location
    start = None
    for i in range(len(lines)):
        line = lines[i]
        if "S" not in line:
            continue
        start = (i, line.index("S"))
    
    if start is None:
        raise ValueError("Invalid Input. No Starting Location")

    # Step 2, get path around starting location
    indexes_around_start = [(start[0] - 1, start[1]), (start[0], start[1] - 1), (start[0], start[1] + 1), (start[0] + 1, start[1])]
    points_into_start = [tile for tile in indexes_around_start if pointsInto(lines[tile[0]][tile[1]], tile, start)]
    if len(points_into_start) != 2:
        raise ValueError("Invalid Input. Starting Location doesn't have exactly 2 connected tiles")
    
    points = [start, points_into_start[0]]
    while lines[points[-1][0]][points[-1][1]] != "S":
        tile = lines[points[-1][0]][points[-1][1]]
        locations = tilePoints(tile, points[-1])
        new_location = locations[1] if points[-2] == locations[0] else locations[0]
        points.append(new_location)
    
    max_y = max([p[0] for p in points])
    min_y = min([p[0] for p in points])
    max_x = max([p[1] for p in points])
    min_x = min([p[1] for p in points])

    def oddEvenTest(point: tuple[int, int]):
        count = 0
        for ray in range(0, point[0]):
            if (ray, point[1]) in points and lines[ray][point[1]] != "|":
                count += 1

        return count
    
    inside = 0
    for i in tqdm(range(min_y, max_y + 1)):
        for j in range(min_x, max_x + 1):
            if (i, j) in points: # Skip points in loop
                continue

            if oddEvenTest((i, j)) % 2 == 1:
                inside += 1
    return inside

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
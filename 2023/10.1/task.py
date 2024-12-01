# https://adventofcode.com/2023/day/9
import os

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
    
    count = 1
    prev_index = start
    current_index = points_into_start[0]
    while lines[current_index[0]][current_index[1]] != "S":
        count += 1
        tile = lines[current_index[0]][current_index[1]]
        locations = tilePoints(tile, current_index)
        new_location = locations[1] if prev_index == locations[0] else locations[0]
        
        prev_index = current_index
        current_index = new_location
    return int(count / 2)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
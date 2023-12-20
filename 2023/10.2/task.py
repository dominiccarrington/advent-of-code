# https://adventofcode.com/2023/day/10
import os
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(it):
        return it

TILES = ["|", "-", "L", "J", "7", "F"]

def directionOfMovement(point1, point2):
    match (point1[0] - point2[0], point1[1] - point2[1]):
        case (0, 1):
            return "W"
        case (0, -1):
            return "E"
        case (1, 0):
            return "N"
        case (-1, 0):
            return "S"

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
    directions = [None, [directionOfMovement(points[0], points[1])]]

    while lines[points[-1][0]][points[-1][1]] != "S":
        current_location = points[-1]
        tile = lines[current_location[0]][current_location[1]]
        connected = tilePoints(tile, current_location)
        new_location = connected[1] if points[-2] == connected[0] else connected[0]

        direction = directionOfMovement(current_location, new_location)
        if directions[-1][0] != direction:
            directions[-1].append(direction)

        directions.append([direction])
        points.append(new_location)
    points.pop(0)
    directions.pop(0)

    max_y = max([p[0] for p in points])
    min_y = min([p[0] for p in points])
    max_x = max([p[1] for p in points])
    min_x = min([p[1] for p in points])

    # https://en.wikipedia.org/wiki/Nonzero-rule
    def windingNumber(point: tuple[int, int]):
        windingNum = 0
        for x in range(point[1], max_x + 1):
            loc = (point[0], x)
            if loc not in points:
                continue
            d = directions[points.index(loc)]
            windingNum += 1 if "N" in d else (-1 if "S" in d else 0)
            
        return windingNum

    inside = []
    for i in tqdm(range(min_y, max_y + 1)):
        for j in range(min_x, max_x + 1):
            check = (i, j)
            if check in points:
                continue
            if windingNumber(check) != 0:
                inside.append(check)

    while True:
        noUpdates = True
        for p in inside:
            connected = [(p[0] - 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1), (p[0] + 1, p[1])]
            if not all([c in inside or c in points for c in connected]):
                inside.remove(p)
                noUpdates = False

        if noUpdates:
            break

    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            p = (i, j)
            if p in inside:
                print("I", end="")
            elif p in points:
                print(lines[i][j], end="")
            else:
                print(".", end="")
        print("\n", end="")
    return len(inside)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
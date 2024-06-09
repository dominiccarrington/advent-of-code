# https://adventofcode.com/2015/day/3
import os

def parseLine(line: str) -> int:
    count = 1
    visited = {}
    visited[0] = {}
    visited[0][0] = True

    santa = (0, 0)
    roboSanta = (0, 0)

    santasTurn = True
    for c in line:
        move = santa if santasTurn else roboSanta
        if c == "^":
            move = (move[0] - 1, move[1])
        elif c == "v":
            move = (move[0] + 1, move[1])
        elif c == ">":
            move = (move[0], move[1] + 1)
        elif c == "<":
            move = (move[0], move[1] - 1)

        if santasTurn:
            santa = move
        else:
            roboSanta = move
        
        (x, y) = move
        if x not in visited:
            visited[x] = {}
        if y not in visited[x]:
            visited[x][y] = True
            count += 1
        santasTurn = not santasTurn

    return count

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(line) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2023/day/8
import os
import re

def parseFile(lines: list):
    directions = lines.pop(0).strip()
    lines.pop(0) # Empty line in input

    graph = {}
    for line in lines:
        matches = re.match(
            r"(\w{3}) = \((\w{3}), (\w{3})\)",
            line.strip(),
        )
        node = matches.group(1)
        leftNode = matches.group(2)
        rightNode = matches.group(3)
        graph[node] = (leftNode, rightNode)
    
    current_node = "AAA"
    count = 0
    while (current_node != "ZZZ"):
        direction = directions[count % len(directions)]
        direction_index = 0 if direction == "L" else 1

        current_node = graph[current_node][direction_index]

        count += 1
    return count

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
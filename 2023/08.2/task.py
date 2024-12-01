# https://adventofcode.com/2023/day/8
import os
import re
import numpy as np

def parseFile(lines: list):
    directions = lines.pop(0).strip()
    lines.pop(0) # Empty line in input

    graph = {}
    current_nodes = []
    for line in lines:
        matches = re.match(
            r"(\w{3}) = \((\w{3}), (\w{3})\)",
            line.strip(),
        )
        node = matches.group(1)
        leftNode = matches.group(2)
        rightNode = matches.group(3)

        graph[node] = (leftNode, rightNode)
        if node.endswith('A'):
            current_nodes.append(node)

    loop_counts = []
    for node in current_nodes:
        current_node = str(node)
        count = 0
        while not current_node.endswith('Z'):
            direction = directions[count % len(directions)]
            direction_index = 0 if direction == "L" else 1
            current_node = graph[current_node][direction_index]
            count += 1
        end_node = current_node
        last_count = count
        loop_counts.append(count)

        print("{} -> {} in {}".format(node, current_node, count))
        for i in range(1, 4):
            direction = directions[count % len(directions)]
            direction_index = 0 if direction == "L" else 1
            current_node = graph[current_node][direction_index]
            count += 1
            while current_node != end_node:
                direction = directions[count % len(directions)]
                direction_index = 0 if direction == "L" else 1
                current_node = graph[current_node][direction_index]
                count += 1

            loop_count = count - last_count
            last_count = count

            print("  Loop {} in {}".format(i, loop_count))

    print(loop_counts)
    return np.lcm.reduce(loop_counts)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
# https://adventofcode.com/2015/day/9
import os
import re
import math

def parseLine(graph, line):
    matches = re.match(r"(\w+) to (\w+) = (\d+)", line)
    if matches is None:
        raise ValueError(line)
    
    from_node = matches.group(1)
    to_node = matches.group(2)
    weight = int(matches.group(3))

    if from_node not in graph:
        graph[from_node] = {}
    if to_node not in graph:
        graph[to_node] = {}
    
    graph[from_node][to_node] = weight
    graph[to_node][from_node] = weight

def parseFile(contents: str) -> int:
    graph = {}
    for line in contents.splitlines():
        parseLine(graph, line)
    
    def dfs(path: list[str] = [], weight = 0):
        if all([n in path for n in graph]):
            return weight

        min_weight = math.inf
        out_nodes = graph[path[-1]].keys()
        out_nodes_not_reached = [n for n in out_nodes if n not in path]
        for n in out_nodes_not_reached:
            copy = [p for p in path]
            copy.append(n)
            min_weight = min(min_weight, dfs(copy, weight + graph[path[-1]][n]))
        return min_weight

    min_weight = math.inf
    for n in graph:
        min_weight = min(dfs([n]), min_weight)
    return min_weight

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
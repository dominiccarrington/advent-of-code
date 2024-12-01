# https://adventofcode.com/2015/day/11
import os
import re
import math

type AdjacencyList = dict[str, dict[str, int]];

def parseLine(line: str):
    matches = re.match(r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)", line)

    if matches is None:
        raise ValueError()
    
    person_a = matches.group(1)
    modifier = matches.group(2)
    value = matches.group(3)
    person_b = matches.group(4)

    return (person_a, person_b, (1 if modifier == "gain" else -1) * int(value))

MYSELF = "_Myself"

def parseFile(contents: str) -> int:
    graph: AdjacencyList = {}
    edges = [parseLine(line) for line in contents.splitlines()]
    for (a, b, w) in edges:
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = w

    nodes = [a for a in graph.keys()]
    graph[MYSELF] = {}
    for n in nodes:
        graph[MYSELF][n] = 0
        graph[n][MYSELF] = 0
    def dfs(node, weight = 0, visited: list[str] = []):
        visited.append(node)

        non_visited_nodes = [n for (n, _) in graph[node].items() if n not in visited]
        if len(non_visited_nodes) > 0:
            return max([
                dfs(n, weight + graph[node][n] + graph[n][node], [v for v in visited]) 
                for n in non_visited_nodes
            ])
        elif visited[0] in graph[node]:
            return weight + graph[node][visited[0]] + graph[visited[0]][node]
        else:
            return -math.inf

    return max([dfs(node) for node in nodes])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
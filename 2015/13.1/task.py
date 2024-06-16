# https://adventofcode.com/2015/day/11
import os
import re
import networkx as nx

type AdjacencyList = dict[str, list[(str, int)]];

def parseLine(line: str):
    matches = re.match(r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)", line)

    if matches is None:
        raise ValueError()
    
    person_a = matches.group(1)
    modifier = matches.group(2)
    value = matches.group(3)
    person_b = matches.group(4)

    return (person_a, person_b, (1 if modifier == "gain" else -1) * int(value))

def parseFile(contents: str) -> int:
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([parseLine(line) for line in contents.splitlines()])
    cycles = nx.recursive_simple_cycles(graph)
    full_cycles = [c for c in cycles if len(c) == len(graph.nodes)]
    
    maximum = 0
    for cycle in full_cycles:
        weight_of_cycle = 0
        for i in range(1, len(cycle)):
            a = cycle[i-1]
            b = cycle[i]
            w = graph[a][b]['weight']
            weight_of_cycle += w
        
        a = cycle[len(cycle) - 1]
        b = cycle[0]
        w = graph[a][b]['weight']
        weight_of_cycle += w
        
        maximum = max(weight_of_cycle, maximum)
    return maximum

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
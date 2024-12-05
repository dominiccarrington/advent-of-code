# https://adventofcode.com/2024/day/5
from math import floor
import os
import networkx as nx
import matplotlib.pyplot as plt

orderingRules: dict[int, set[int]] = {}

def parseOrderingRule(line: str):
    a, b = [int(x) for x in line.split('|')]
    if b in orderingRules:
        orderingRules[b].add(a)
    else:
        orderingRules[b] = set([a])

def fixOrder(order: list[int]) -> int:
    noRestriction = [pageNo for pageNo in order if pageNo not in orderingRules.keys()]

    graph = nx.DiGraph()
    graph.add_nodes_from(order)
    graph.add_edges_from([
        (y, x)
        for x in order
        if x in orderingRules.keys()
        for y in orderingRules[x]
        if y in order
    ])

    newOrder = list(noRestriction)
    graph.remove_nodes_from(newOrder)

    while len(graph.nodes):
        nodeDegrees = list(graph.in_degree(order))
        for node, count in nodeDegrees:
            if count == 0:
                newOrder.append(node)
                graph.remove_node(node)

    return newOrder

def parseUpdate(line: str) -> int:
    order = [int(x) for x in line.split(',')]

    for index, pageNumber in enumerate(order):
        if pageNumber not in orderingRules:
            continue
        printedAfter = order[index:]
        requiredBefore = orderingRules[pageNumber]
        if not requiredBefore.isdisjoint(set(printedAfter)):
            fixedOrder = fixOrder(order)
            return fixedOrder[floor(len(fixedOrder) / 2)]

    return 0

def parseFile(fileContents: str) -> int:
    answer = 0
    for line in fileContents.splitlines():
        if ',' in line:
            answer += parseUpdate(line)
        elif '|' in line:
            parseOrderingRule(line)
    
    return answer

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
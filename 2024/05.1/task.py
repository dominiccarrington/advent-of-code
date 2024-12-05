# https://adventofcode.com/2024/day/5
from math import floor
import os

orderingRules: dict[int, set[int]] = {}

def parseOrderingRule(line: str):
    a, b = [int(x) for x in line.split('|')]
    if b in orderingRules:
        orderingRules[b].add(a)
    else:
        orderingRules[b] = set([a])

def parseUpdate(line: str) -> int:
    order = [int(x) for x in line.split(',')]

    for index, pageNumber in enumerate(order):
        if pageNumber not in orderingRules:
            continue
        printedAfter = order[index:]
        requiredBefore = orderingRules[pageNumber]
        if not requiredBefore.isdisjoint(set(printedAfter)):
            return 0

    return order[floor(len(order) / 2)]

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
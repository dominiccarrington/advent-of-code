# https://adventofcode.com/2023/day/12
import os
import re

def expand(positions):
    expanded = [""]
    for chars in positions:
        newExpanded = []
        for c in chars:
            for e in expanded:
                newExpanded.append(e+c)
        expanded = newExpanded
    return expanded

def parseLine(line: str):
    [row, groups] = line.split()
    groups = [int(i) for i in groups.split(",")]

    # We don't care how many . are between ?# groups
    row = re.sub(r"\.+", '.', row)

    def isValid(row):
        rowGroups = [r for r in row.split('.') if r != '']
        # print(row, rowGroups, groups, sep=" || ")
        return len(rowGroups) == len(groups) and all([
            len(rowGroups[i]) == groups[i] or str(rowGroups[i]).count('#') == groups[i]
            for i in range(len(rowGroups))
        ])

    if isValid(row):
        return 1

    return len([option for option in expand([[".", "#"] if c =="?" else [c] for c in row]) if isValid(option)])

def parseFile(lines: list[str]):
    return sum([parseLine(line.strip()) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

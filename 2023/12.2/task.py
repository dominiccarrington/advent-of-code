# https://adventofcode.com/2023/day/12
import os
import re
from tqdm import tqdm
from multiprocessing import Pool

def parseRow(row: str, groups: list[int], count = 0) -> int:
    nonEmptyGroups = [g for g in groups if g is not None and g > 0]

    requiredChars = max(0, sum(nonEmptyGroups) + len(nonEmptyGroups) - 1)
    if requiredChars > len(row):
        # Too few characters remaining in row
        return count

    if row == "":
        return count + (1 if len(nonEmptyGroups) == 0 else 0)
    
    if len(nonEmptyGroups) == 0:
        return count + (0 if "#" in row else 1)

    if row[-1] == ".":
        if groups[-1] is not None and groups[-1] > 0:
            return count
        
        if groups[-1] is not None:
            groups.pop()
            groups.append(None)
        return parseRow(row[:-1], groups, count)
    elif row[-1] == "#":
        if groups[-1] is None:
            groups.pop()
        
        if groups[-1] == 0:
            return count
        row = row[:-1]
        groups[-1] -= 1
        return parseRow(row, groups, count)
    elif row[-1] == "?":
        t = parseRow(row[:-1] + ".", groups.copy(), count) if groups[-1] is None or groups[-1] == 0 else 0

        if groups[-1] is None and len(groups) >= 2:
            nextGroupLen = groups[-2]
            if len(row) >= nextGroupLen:
                nextGroup = row[-nextGroupLen:]
                if "." not in nextGroup and (len(row) == nextGroupLen or row[-nextGroupLen-1] == "." or row[-nextGroupLen-1] == "?"):
                    groups.pop(-2)
                    return t + parseRow(row[:-nextGroupLen-1], groups.copy(), count)

        return t + parseRow(row[:-1] + "#", groups.copy(), count)

def parseLine(line: str):
    [r, groups] = line.split()
    row = ""
    for i in range(5):
        row += r
        row += "?" if i < 4 else ""

    groups = [int(i) for i in groups.split(",")]
    groups *= 5

    # We don't care how many . are between ?# groups
    row = re.sub(r"\.+", '.', row)

    if row.startswith("."):
        row = row[1:]
    if row.endswith("."):
        row = row[:-1]

    groups.append(None)
    options = parseRow(row, groups)
    return options

def parseFile(lines: list[str]):
    with Pool(processes=10) as p:
        output_values = list(tqdm(p.imap_unordered(parseLine, [line.strip() for line in lines]), total=len(lines)))
        return sum(output_values)

    # return sum([parseLine(line.strip()) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main()

# https://adventofcode.com/2015/day/19
import os
import re
import math

def solve(replacements: dict[str, list[str]], input: str) -> int:
    values = set()
    max_chars = max([len(k) for k in replacements.keys()])
    for i in range(1, max_chars + 1):
        for c in range(0, len(input) - i + 1):
            check = input[c:c+i]
            if check not in replacements:
                continue

            for r in replacements[check]:
                new_string = f"{input[0:c]}{r}{input[c+i:len(input)-1]}"
                values.add(new_string)
        
    return len(values)

def parseFile(contents: str) -> int:
    replacements: dict[str, list[str]] = {}
    input = ""

    reading_replacements = True
    for line in contents.splitlines():
        if line.strip() == "":
            reading_replacements = False
            continue
        if reading_replacements:
            matches = re.match(r"(\w+) => (\w+)", line)
            if matches is None:
                raise ValueError
            replace = matches.group(1)
            if replace not in replacements:
                replacements[replace] = []
            replacements[replace].append(matches.group(2))
        else:
            input = line
            break
    
    return solve(replacements, input)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
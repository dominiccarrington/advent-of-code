# https://adventofcode.com/2015/day/5
import os

VOWELS = ["a", "e", "i", "o", "u"]
DENYLIST_STRINGS = ["ab", "cd", "pq", "xy"]

def _checkDenyList(line):
    return any([s in line for s in DENYLIST_STRINGS])

def _countVowels(line):
    return sum([line.count(v) for v in VOWELS])

def parseLine(line: str):
    if _checkDenyList(line):
        return 0

    vowels = _countVowels(line)
    if vowels < 3:
        return 0

    for i in range(0, len(line)-1):
        if line[i] == line[i+1]:
            # This is the final check therefore we can return.
            return 1
        
    return 0

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(l) for l in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2015/day/11
import os
import json

def parse(a) -> int:
    if type(a) == list:
        return parseList(a)
    elif type(a) == dict:
        return parseDict(a)
    elif type(a) == int:
        return int(a)
    else:
        return 0

def parseList(a: list) -> int:
    return sum([parse(el) for el in a])

def parseDict(a: dict) -> int:
    # Return 0 early
    for value in a.values():
        if value == "red":
            return 0
    
    return sum([parse(value) for value in a.values()])

def parseFile(pwd: str) -> str:
    o = json.loads(pwd)
    return parse(o)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2015/day/8
import os

def parseLine(line: str):
    if line[0] != '"':
        return 0
    if line[-1] != '"':
        return 0
    str_contents = line[1:-1]
    
    count = 0
    i = 0
    while i < len(str_contents):
        c = str_contents[i]
        if c == "\\":
            if str_contents[i+1] == "x":
                i += 3
            else:
                i += 1
        count += 1
        i += 1
    return len(line) - count

def parseFile(lines: list[str]) -> int:
    return sum([parseLine(l.strip()) for l in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
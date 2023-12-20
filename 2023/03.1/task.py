# https://adventofcode.com/2023/day/3
import os

SYMBOLS = "! £ $ % ^ & * _ + - = # ~ @ / ? > < : ; | \\ [ ] { }".split()
DIGITS = "0 1 2 3 4 5 6 7 8 9".split()

def findNumber(line, charStart):
    number = line[charStart]
    
    back = 1
    while charStart - back >= 0 and line[charStart - back] in DIGITS:
        number = line[charStart - back] + number
        back += 1

    forward = 1
    while charStart + forward < len(line) and line[charStart + forward] in DIGITS:
        number += line[charStart + forward]
        forward += 1

    return int(number)

def parseFile(contents: list[str]) -> int:
    lines = [line.strip() for line in contents]

    sigma = 0
    for lineNo in range(0, len(lines)):
        line = lines[lineNo]
        for charNo in range(0, len(line)):
            char = line[charNo]
            if char not in SYMBOLS:
                continue
            searchOptions = [coords for coords in [
                [lineNo - 1 , charNo - 1], [lineNo - 1  , charNo] , [lineNo - 1   , charNo + 1],
                [lineNo     , charNo - 1], [lineNo      , charNo] , [lineNo       , charNo + 1],
                [lineNo + 1 , charNo - 1], [lineNo + 1  , charNo] , [lineNo + 1   , charNo + 1],
            ] if coords is not None]
            
            match = {}
            for coords in searchOptions:
                maybeDigit = lines[coords[0]][coords[1]]
                if maybeDigit not in DIGITS:
                    match[coords[0]] = False
                    continue
                elif match.get(coords[0], False):
                    continue
                match[coords[0]] = True

                sigma += findNumber(lines[coords[0]], coords[1])

    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
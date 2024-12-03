# https://adventofcode.com/2024/day/3
import os
import re

pattern = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

def parseFile(fileContents: str) -> int:
    sumOfMul = 0
    active = True
    for line in fileContents.splitlines():
        for m in pattern.finditer(line):
            if m.group(4) == "do":
                active = True
            elif m.group(5) == "don't":
                active = False
            elif m.group(1) == "mul" and active:
                sumOfMul += int(m.group(2)) * int(m.group(3))
    return sumOfMul

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2023/day/14
import os
import re

def hash(text: str) -> int:
    currentValue = 0
    for c in text:
        ascii = ord(c)
        currentValue += ascii
        currentValue *= 17
        currentValue %= 256

    return currentValue

def parseFile(input: str):
    map = {}
    for operation in input.strip().split(","):
        m = re.match(r"(\w+)([-=])(\d)?", operation)
        (label, operation, focalLength) = m.groups()
        hashValue = hash(label)

        if operation == "=":
            if hashValue not in map.keys():
                map[hashValue] = []
            
            if label in [s for (s, _) in map[hashValue]]:
                for i in range(len(map[hashValue])):
                    if map[hashValue][i][0] == label:
                        map[hashValue][i][1] = focalLength
                        break
            else:
                map[hashValue].append([label, focalLength])
        elif operation == "-":
            if hashValue in map.keys():
                i = 0
                while i < len(map[hashValue]):
                    if map[hashValue][i][0] == label:
                        break
                    i += 1
                if i < len(map[hashValue]):
                    del map[hashValue][i]

    sigma = 0
    for box in map.keys():
        for slot in range(len(map[box])):
            sigma += (box + 1) * (slot + 1) * int(map[box][slot][1])
    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()

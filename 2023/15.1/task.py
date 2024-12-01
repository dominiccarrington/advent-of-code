# https://adventofcode.com/2023/day/14
import os

def hash(text: str) -> int:
    currentValue = 0
    for c in text:
        ascii = ord(c)
        currentValue += ascii
        currentValue *= 17
        currentValue %= 256

    return currentValue

def parseFile(input: str):
    return sum([hash(i) for i in input.strip().split(",")])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()

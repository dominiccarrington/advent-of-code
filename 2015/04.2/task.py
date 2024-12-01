# https://adventofcode.com/2015/day/4
import os
import hashlib

def parseFile(file_contents: str) -> int:
    # There must be a better way to do this???
    i = 0
    while True:
        s = file_contents + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h.startswith("000000"):
            return i
        i += 1

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
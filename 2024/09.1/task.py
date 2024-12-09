# https://adventofcode.com/2024/day/9
import os
from timeit import timeit

def parseFile(fileContents: str) -> int:
    totalBlocks = sum([int(fileContents[i]) for i in range(0, len(fileContents), 2)])
    forwardPointer = [0, int(fileContents[0])]
    backwardPointer = [len(fileContents) - 1, int(fileContents[-1])]
    s = 0
    i = 0
    while forwardPointer[0] < backwardPointer[0]:
        if forwardPointer[0] % 2 == 0:
            s += i * int(forwardPointer[0] / 2)
        else:
            s += i * int(backwardPointer[0] / 2)
            backwardPointer[1] -= 1
            while backwardPointer[1] == 0:
                backwardPointer[0] -= 2
                backwardPointer[1] = int(fileContents[backwardPointer[0]])

        forwardPointer[1] -= 1
        while forwardPointer[1] == 0:
            forwardPointer[0] += 1
            forwardPointer[1] = int(fileContents[forwardPointer[0]])
        i += 1
    for j in range(i, totalBlocks):
        s += j * int(forwardPointer[0] / 2)
    return s

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    time = timeit(main, 'gc.enable()', number=1)
    print(f"Time Taken: {time} secs")
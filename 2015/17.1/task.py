# https://adventofcode.com/2015/day/16
import os
import re
import math

AMOUNT_OF_EGGNOG = 150

def solve(containers: list[int], amount_remaining: int):
    count = 0
    for i in range(0, len(containers)):
        container = containers[i]
        if container == amount_remaining:
            count += 1
        elif amount_remaining - container < 0:
            break
        elif amount_remaining - container > 0:
            count += solve(containers[i+1:], amount_remaining - container)
    return count

def parseFile(contents: str) -> int:
    containers = [int(size) for size in contents.splitlines()]
    containers.sort()
    return solve(containers, AMOUNT_OF_EGGNOG)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
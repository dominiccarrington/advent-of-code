# https://adventofcode.com/2015/day/16
import os
import re
import math

AMOUNT_OF_EGGNOG = 150

def solve(containers: list[int], amount_remaining: int, depth = 1):
    ret = (math.inf, 0)
    for i in range(0, len(containers)):
        container_size = containers[i]
        if amount_remaining < container_size:
            # The array is sorted therefore all containers
            # past this point are also going to fail at this point
            break
        elif amount_remaining == container_size:
            if depth == ret[0]:
                ret = (ret[0], ret[1] + 1)
            elif depth < ret[0]:
                ret = (depth, 1)
        elif amount_remaining > container_size:
            (length, count) = solve(containers[i+1:], amount_remaining - container_size, depth + 1)
            if length == ret[0]:
                ret = (ret[0], ret[1] + count)
            elif length < ret[0]:
                ret = (length, count)
    return ret

def parseFile(contents: str) -> int:
    containers = [int(size) for size in contents.splitlines()]
    containers.sort()

    
    (_, count) = solve(containers, AMOUNT_OF_EGGNOG)
    return count

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
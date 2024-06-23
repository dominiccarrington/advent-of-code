# https://adventofcode.com/2015/day/23
import os
import re
import math
import itertools
from functools import reduce

NUMBER_OF_COMPARTMENTS = 4

def parseFile(contents: str) -> int:
    presents_weight = sorted([int(line) for line in contents.splitlines()], reverse=True)
    presents_weight_sum = sum(presents_weight)
    if presents_weight_sum % NUMBER_OF_COMPARTMENTS > 0:
        raise ValueError()
    
    weight_of_each_compartment = presents_weight_sum / NUMBER_OF_COMPARTMENTS
    prefix: dict[int, list[list[int]]] = {}
    min_length = math.inf
    remaining_weight = sum(presents_weight)
    for i in range(0, len(presents_weight)):
        present_weight = presents_weight[i]
        if 0 in prefix:
            min_length = min(len(l) for l in prefix[0])
        keys = [l for l in prefix.keys() if l <= remaining_weight]

        for n in keys:
            amount_remaining = n - present_weight
            if amount_remaining < 0:
                continue
            copy = [list(l) for l in prefix[n] if len(l) < min_length and present_weight not in l]
            for c in copy:
                c.append(present_weight)
            if amount_remaining not in prefix:
                prefix[amount_remaining] = copy
            else:
                prefix[amount_remaining].extend(copy)

        amount_remaining = weight_of_each_compartment - present_weight
        if amount_remaining not in prefix:
            prefix[amount_remaining] = [[present_weight]]
        else:
            prefix[amount_remaining].extend([[present_weight]])
        remaining_weight -= present_weight
    
    if 0 not in prefix:
        return -1
    options = prefix[0]
    min_length = min([len(l) for l in options])
    min_options = [o for o in options if len(o) == min_length]
    return min([reduce((lambda x, y: x * y), v) for v in min_options])


def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
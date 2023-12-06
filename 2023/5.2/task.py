import os
import math
import numpy as np
import pandas as pd
from multiprocessing import Pool
import tqdm

def parseFile(fileName: str) -> int:
    with open(fileName) as f:
        return [[int(n) for n in l.strip().split()] for l in f.readlines()]

def applyMap(value, map) -> int:
    for (dest, src, length) in map:
        if src <= value and value < (src + length):
            return value - src + dest
    return value

def parseSeedRange(seedRange):
    dir = os.path.dirname(__file__)
    (start, length) = seedRange
    
    maps = [
        parseFile(dir + "/inputs/seed-to-soil.txt"),
        parseFile(dir + "/inputs/soil-to-fertilizer.txt"),
        parseFile(dir + "/inputs/fertilizer-to-water.txt"),
        parseFile(dir + "/inputs/water-to-light.txt"),
        parseFile(dir + "/inputs/light-to-temperature.txt"),
        parseFile(dir + "/inputs/temperature-to-humidity.txt"),
        parseFile(dir + "/inputs/humidity-to-location.txt"),
    ]

    m = math.inf
    for seed in range(start, start + length):
        value = seed
        for map in maps:
            value = applyMap(value, map)
        
        m = min(m, value)

    return m

def main():
    dir = os.path.dirname(__file__)

    seedLine = []
    with open(dir + '/inputs/seeds.txt') as f:
        seedLine = [int(n) for n in f.readline().split()]

    seedRanges = [(seedLine[i], seedLine[i+1]) for i in range(0, len(seedLine), 2)]
    
    poolInputs = []
    b = 100000
    for (start, length) in seedRanges:
        while length > b:
            poolInputs.append((start, b))
            start += b
            length -= b
        poolInputs.append((start, length))
    print(len(poolInputs))

    with Pool(processes=100) as p:
        output_values = list(tqdm.tqdm(p.imap_unordered(parseSeedRange, poolInputs), total=len(poolInputs)))
        print(min(output_values))

if __name__ == "__main__":
    main()

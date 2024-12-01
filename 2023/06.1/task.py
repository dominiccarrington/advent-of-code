# https://adventofcode.com/2023/day/4
import os
import functools

def parseRace(time, distanceRecord) -> int:
    count = 0
    for i in range(time):
        if i * (time - i) > distanceRecord:
            count += 1
    return count

def main():
    dir = os.path.dirname(__file__)

    with open(dir + '/input.txt') as f:
        times = [int(t) for t in f.readline().split()]
        distance = [int(d) for d in f.readline().split()]

    product = functools.reduce(lambda carry, value: carry * value, [parseRace(time, distance) for (time, distance) in zip(times, distance)])
    print(product)

if __name__ == "__main__":
    main();
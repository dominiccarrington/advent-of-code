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
    time = 60_947_882
    distance = 475_213_810_151_650
    print(parseRace(time, distance))

if __name__ == "__main__":
    main();
# https://adventofcode.com/2015/day/14
import os
import re
import math

LENGTH_OF_RACE = 2503

def parseLine(line: str):
    matches = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    if matches is None:
        raise ValueError
    
    name = matches.group(1)
    fly_speed = int(matches.group(2))
    fly_duration = int(matches.group(3))
    rest_duration = int(matches.group(4))

    full_distance = fly_speed * fly_duration
    full_duration = fly_duration + rest_duration

    number_of_full_distances = math.floor(LENGTH_OF_RACE / full_duration)
    full_blocks_travelled = number_of_full_distances * full_distance

    overtime = LENGTH_OF_RACE - (number_of_full_distances * full_duration)
    extra_movement_time = min(fly_duration, overtime)
    extra_movement = extra_movement_time * fly_speed

    return full_blocks_travelled + extra_movement

def parseFile(contents: str) -> int:
    return max([parseLine(line) for line in contents.splitlines()])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
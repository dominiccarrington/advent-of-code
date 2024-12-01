# https://adventofcode.com/2015/day/14
import os
import re
import math

LENGTH_OF_RACE = 2503

class Reindeer:
    is_flying = True
    duration_remaining = 0

    distance_travelled = 0
    points = 0

    def __init__(self, fly_speed, fly_duration, rest_duration):
        self.fly_speed = fly_speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration

        self.duration_remaining = self.fly_duration

    def tick(self):
        if self.is_flying:
            self.distance_travelled += self.fly_speed
            
        self.duration_remaining -= 1
        if self.duration_remaining == 0:
            self.is_flying = not self.is_flying
            self.duration_remaining = self.fly_duration if self.is_flying else self.rest_duration


def parseLine(line: str):
    matches = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    if matches is None:
        raise ValueError
    
    name = matches.group(1)
    fly_speed = int(matches.group(2))
    fly_duration = int(matches.group(3))
    rest_duration = int(matches.group(4))

    return (name, Reindeer(fly_speed, fly_duration, rest_duration))

def parseFile(contents: str) -> int:
    reindeer = [parseLine(line)[1] for line in contents.splitlines()]
    
    for _ in range(LENGTH_OF_RACE):
        for r in reindeer:
            r.tick()
        
        ordered = sorted(
            reindeer,
            key=lambda r : r.distance_travelled,
            reverse=True
        )
        max_distance = ordered[0].distance_travelled
        i = 0
        while ordered[i].distance_travelled == max_distance:
            ordered[i].points += 1
            i += 1
    
    return max([r.points for r in reindeer])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
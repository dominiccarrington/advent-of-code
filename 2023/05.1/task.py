# https://adventofcode.com/2023/day/5
import os

dir = os.path.dirname(__file__)

parsedFiles = {}
def parseFile(fileName: str, searchNumber: int) -> int:
    if not fileName in parsedFiles:
        with open(dir + '/' + fileName) as f:
            parsedFiles[fileName] = [[int(n) for n in l.strip().split()] for l in f.readlines()]
        
    for map in parsedFiles[fileName]:
        if map[1] <= searchNumber and searchNumber < (map[1] + map[2]):
            return searchNumber - map[1] + map[0]
    return searchNumber

def humidityToLocation(humidity: int) -> int:
    return parseFile('inputs/humidity-to-location.txt', humidity)

def temperatureToHumidity(temperature: int) -> int:
    return parseFile('inputs/temperature-to-humidity.txt', temperature)

def lightToTemperature(light: int) -> int:
    return parseFile('inputs/light-to-temperature.txt', light)

def waterToLight(water: int) -> int:
    return parseFile('inputs/water-to-light.txt', water)

def fertilizerToWater(fertilizer: int) -> int:
    return parseFile('inputs/fertilizer-to-water.txt', fertilizer)

def soilToFertilizer(soil: int) -> int:
    return parseFile('inputs/soil-to-fertilizer.txt', soil)

def seedToSoil(seed: int) -> int:
    return parseFile('inputs/seed-to-soil.txt', seed)


def main():
    seeds = []
    with open(dir + '/inputs/seeds.txt') as f:
        seeds = [int(n) for n in f.readline().split()]
    
    soils = [seedToSoil(i) for i in seeds]
    fertilizers = [soilToFertilizer(i) for i in soils]
    waters = [fertilizerToWater(i) for i in fertilizers]
    lights = [waterToLight(i) for i in waters]
    temps = [lightToTemperature(i) for i in lights]
    humidities = [temperatureToHumidity(i) for i in temps]
    locations = [humidityToLocation(i) for i in humidities]

    print(min(locations))

if __name__ == "__main__":
    main();
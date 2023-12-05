# https://adventofcode.com/2023/day/5
import os
import math

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

def revParseFile(fileName: str, resNumber: int) -> int:
    if not fileName in parsedFiles:
        with open(dir + '/' + fileName) as f:
            parsedFiles[fileName] = [[int(n) for n in l.strip().split()] for l in f.readlines()]
        
    for map in parsedFiles[fileName]:
        if map[0] <= resNumber and resNumber < (map[0] + map[2]):
            return resNumber - map[0] + map[1]
    return resNumber

def humidityToLocation(humidity: int) -> int:
    return parseFile('inputs/humidity-to-location.txt', humidity)
def locationToHumidity(location: int) -> int:
    return revParseFile('inputs/humidity-to-location.txt', location)

def temperatureToHumidity(temperature: int) -> int:
    return parseFile('inputs/temperature-to-humidity.txt', temperature)
def humidityToTemperature(humidity: int) -> int:
    return revParseFile('inputs/temperature-to-humidity.txt', humidity)

def lightToTemperature(light: int) -> int:
    return parseFile('inputs/light-to-temperature.txt', light)
def temperatureToLight(temp: int) -> int:
    return revParseFile('inputs/light-to-temperature.txt', temp)

def waterToLight(water: int) -> int:
    return parseFile('inputs/water-to-light.txt', water)
def lightToWater(light: int) -> int:
    return revParseFile('inputs/water-to-light.txt', light)

def fertilizerToWater(fertilizer: int) -> int:
    return parseFile('inputs/fertilizer-to-water.txt', fertilizer)
def waterToFertilizer(water: int) -> int:
    return revParseFile('inputs/fertilizer-to-water.txt', water)

def soilToFertilizer(soil: int) -> int:
    return parseFile('inputs/soil-to-fertilizer.txt', soil)
def fertilizerToSoil(fertilizer: int) -> int:
    return revParseFile('inputs/soil-to-fertilizer.txt', fertilizer)

def seedToSoil(seed: int) -> int:
    return parseFile('inputs/seed-to-soil.txt', seed)
def soilToSeed(soil: int) -> int:
    return revParseFile('inputs/seed-to-soil.txt', soil)

def main():
    seedsLine = []
    with open(dir + '/inputs/seeds.txt') as f:
        seedsLine = [int(n) for n in f.readline().split()]
    
    lowestSeedNumber = min([seedsLine[j] for j in range(0, len(seedsLine), 2)])
    largestSeedNumber = max([seedsLine[j] + seedsLine[j+1] for j in range(0, len(seedsLine), 2)])
    
    location = -1
    seed = 0
    while seed == 0:
        location += 1

        humidity = locationToHumidity(location)
        temp = humidityToTemperature(humidity)
        light = temperatureToLight(temp)
        water = lightToWater(light)
        fertilizer = waterToFertilizer(water)
        soil = fertilizerToSoil(fertilizer)
        seed = soilToSeed(soil)

        if lowestSeedNumber <= seed and seed <= largestSeedNumber:
            for i in range(0, len(seedsLine), 2):
                if not (int(seedsLine[i]) <= seed and seed < int(seedsLine[i+1])):
                    seed = 0

    print(location)

if __name__ == "__main__":
    main();
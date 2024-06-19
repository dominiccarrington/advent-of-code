# https://adventofcode.com/2015/day/19
import os
import re
import math
import itertools

PRIME_NUMBERS = [2, 3, 5, 7, 11, 13] # ...
def primeNumbers():
    for number in PRIME_NUMBERS:
        yield number
    
    while True:
        number += 2
        prime = True
        for prime in PRIME_NUMBERS:
            if number % prime == 0:
                prime = False
                break
        if prime:
            PRIME_NUMBERS.append(number)
            yield number

def primeFactors(number: int) -> list[int]:
    if number == 1:
        return []
    
    if number in PRIME_NUMBERS:
        return [number]
    
    factors = []
    for prime in primeNumbers():
        while number % prime == 0:
            number /= prime
            factors.append(prime)
        if number == 1 or prime > number:
            break
    return factors

def presentsForHouse(house_number: int) -> int:
    presents = 10 # Always visited by Elf 1
    factors = primeFactors(house_number)
    for i in range(1, len(factors) + 1):
        combinations = itertools.combinations(factors, i)
        for c in combinations:
            presents += sum([i * 10 for i in c])

    return presents

def parseFile(contents: str) -> int:
    threshold = int(contents)
    presents = 0
    i = 1
    while presents < threshold:
        i += 1
        presents = presentsForHouse(i)

    return i

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
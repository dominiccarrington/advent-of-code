import os
import re

numerals = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

def convertLineToNumber(line: str) -> int:
    i = 0
    first_number = None
    last_number = None
    while i < len(line) and first_number is None:
        for n in numerals.keys():
            if line[i:(i+len(n))] == n:
                first_number = numerals[line[i:(i+len(n))]]
                break
        i += 1

    i = 0
    line = line[::-1]
    while i < len(line) and last_number is None:
        for n in numerals.keys():
            if line[i:(i+len(n))] == n[::-1]:
                last_number = numerals[line[i:(i+len(n))][::-1]]
                break
        i += 1
    
    if first_number is None or last_number is None:
        raise RuntimeError("[{}] first_number ({}) or last_number ({}) are none".format(line, first_number, last_number))

    return (first_number * 10 + last_number)

def main():
    sigma = 0
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        for line in f:
            sigma += convertLineToNumber(line)

    print(sigma)

if __name__ == "__main__":
    main()
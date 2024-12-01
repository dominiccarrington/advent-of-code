# https://adventofcode.com/2023/day/4
import os

def parseLine(line: str) -> int:
    [card, numbers] = [l.strip() for l in line.split(':')]
    [winNumbers, yourNumbers] = [set([int(n) for n in listNumbers.strip().split()]) for listNumbers in numbers.split('|')]
    
    winningNumbers = len(winNumbers & yourNumbers)

    return 0 if winningNumbers == 0 else 2**(winningNumbers-1)

def parseFile(lines: list[str]) -> int:
    sigma = 0
    for line in lines:
        sigma += parseLine(line.strip())
    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main();
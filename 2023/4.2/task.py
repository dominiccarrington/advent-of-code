# https://adventofcode.com/2023/day/4
import os

def parseLine(line: str) -> int:
    [card, numbers] = [l.strip() for l in line.split(':')]
    [winNumbers, yourNumbers] = [set([int(n) for n in listNumbers.strip().split()]) for listNumbers in numbers.split('|')]
    
    winningNumbers = len(winNumbers & yourNumbers)

    return winningNumbers

def parseFile(lines: list[str]) -> int:
    cards = []

    for i in range(0, len(lines)):
        cards.append({
            "matchingNumbers": parseLine(lines[i].strip()),
            "times": 1
        })
    
    sigma = 0
    for i in range(0, len(cards)):
        card = cards[i]
        for _ in range(0, card['times']):
            for j in range(0, card['matchingNumbers']):
                cards[i+j+1]['times'] += 1
        sigma += card['times']

    return sigma

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
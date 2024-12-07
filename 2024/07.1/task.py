# https://adventofcode.com/2024/day/7
import os

operations = [
    lambda a, b: a + b,
    lambda a, b: a * b,
]

def parseLine(line: str) -> int:
    target, numbers = [s.strip() for s in line.split(':')]
    target = int(target)
    numbers = [int(i) for i in numbers.split()]
    
    def check(curr, remaining):
        for op in operations:
            newValue = op(curr, remaining[0])
            if len(remaining) == 1:
                if newValue == target:
                    return True
            elif check(newValue, remaining[1:]):
                return True
        return False
    
    return target if check(numbers[0], numbers[1:]) else 0

def parseFile(fileContents: str) -> int:
   return sum([parseLine(line) for line in fileContents.splitlines()])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
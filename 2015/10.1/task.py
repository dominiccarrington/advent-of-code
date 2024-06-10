# https://adventofcode.com/2015/day/10
import os

def createNewSequence(sequence: str):
    new_sequence = ""
    i = 0
    while i < len(sequence):
        number = sequence[i]
        j = 1
        try:
            while sequence[i+j] == number:
                j += 1
        except IndexError:
            pass
        new_sequence += f"{j}{number}"
        i += j
    return new_sequence

def parseFile(start: str) -> int:
    sequence = start
    for _ in range(0, 40):
        sequence = createNewSequence(sequence)
    return len(sequence)

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
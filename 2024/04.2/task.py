# https://adventofcode.com/2024/day/4
import os

def parseFile(fileContents: str) -> int:
    lines = fileContents.splitlines()

    def look(i, j):
        try:
            positiveDiagonal = (
                (lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S') or
                (lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M')
            )
            negativeDiagonal = (
                (lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S') or
                (lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M')
            )
            return positiveDiagonal and negativeDiagonal
        except IndexError:
            return False

    count = sum([
        look(i, j) 
        for i in range(1, len(lines) - 1) 
        for j in range(1, len(lines[i]) - 1)
        if lines[i][j] == 'A'
    ])
    return count

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
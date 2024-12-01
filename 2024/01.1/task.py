# https://adventofcode.com/2024/day/1
import os

def parseFile(file_contents: str) -> int:
    left_list = []
    right_list = []

    for line in file_contents.splitlines():
        left, right = [int(x) for x in line.split()]
        left_list.append(left)
        right_list.append(right)
    
    left_list.sort()
    right_list.sort()

    diff = 0
    for i in range(len(left_list)):
        diff += abs(left_list[i] - right_list[i])
        
    return diff
        

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
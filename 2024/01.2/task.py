# https://adventofcode.com/2024/day/1
import os

def parseFile(file_contents: str) -> int:
    left_list = []
    right_map = {}

    for line in file_contents.splitlines():
        left, right = [int(x) for x in line.split()]
        left_list.append(left)

        right_map[right] = right_map.get(right, 0) + 1

    similarity = 0
    for num in left_list:
        similarity += num * right_map.get(num, 0)
        
    return similarity
        

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read()))

if __name__ == "__main__":
    main()
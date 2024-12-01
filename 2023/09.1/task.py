# https://adventofcode.com/2023/day/9
import os

def predictNext(nums: list[int]) -> int:
    gaps = []
    for i in range(len(nums) - 1):
        gaps.append(nums[i+1] - nums[i])

    add = gaps[-1] if all([gap == gaps[0] for gap in gaps]) else predictNext(gaps)
    
    return nums[-1] + add

def parseLine(line: str):
    nums = [int(n) for n in line.split()]
    
    return predictNext(nums)

def parseFile(lines: list):
    return sum([parseLine(line.strip()) for line in lines])

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
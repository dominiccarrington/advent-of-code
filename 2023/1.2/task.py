import os
import re

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

numbersRegex = re.compile("(" + "|".join(numbers.keys()) + ")")

def replaceNumericWithInteger(line: str) -> str:
    ## Attempt 1: This fails since it searches for the numbers in order
    ## However, this breaks for cases like "twone". This code turns it
    ## into "tw1" however the correct solution is "2ne"
    ## Answer: 55584
    # for num in numbers.keys():
    #     line = line.replace(num, str(numbers[num]))
    # return line

    ## Attempt 2: This uses regex to convert the strings into the numeric
    ## equivalents however this again has given an answer too low.
    ## Answer: 56001
    return numbersRegex.sub(lambda s: str(numbers[s.group()]), line)

def convertToInteger(str):
    if len(str) > 1:
        return None
    
    try:
        i = int(str)
        
        return i if i > 0 else None
    except ValueError:
        return None

def convertLineToNumber(line):
    line = replaceNumericWithInteger(line)

    i = 0
    first_number = None
    last_number = None
    while i < len(line) and (first_number is None or last_number is None):
        if first_number is None:
            first_number = convertToInteger(line[i])

        if last_number is None:
            last_number = convertToInteger(line[len(line) - i - 1])

        i += 1
    
    if first_number is None or last_number is None:
        raise RuntimeError("[{}] first_number ({}) or last_number ({}) are none".format(line.strip(), first_number, last_number))
    
    return first_number * 10 + last_number

def main():
    sigma = 0
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        for line in f:
            sigma += convertLineToNumber(line)

    print(sigma)

if __name__ == "__main__":
    main()
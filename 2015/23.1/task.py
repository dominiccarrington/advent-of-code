# https://adventofcode.com/2015/day/23
import os
import re
import math

def parseJump(jmp):
    if jmp[0] == "+":
        jmp = jmp[1:]
    return int(jmp)

instruction_parsers = [
    (
        re.compile(r"hlf (a|b)"),
        lambda matches: ("HALF", matches.group(1))
    ),
    (
        re.compile(r"tpl (a|b)"),
        lambda matches: ("TRIPLE", matches.group(1))
    ),
    (
        re.compile(r"inc (a|b)"),
        lambda matches: ("INCREMENT", matches.group(1))
    ),
    (
        re.compile(r"jmp ((?:\+|\-)\d+)"),
        lambda matches: ("JUMP", parseJump(matches.group(1)))
    ),
    (
        re.compile(r"jie (a|b), ((?:\+|\-)\d+)"),
        lambda matches: ("JUMP_EVEN", matches.group(1), parseJump(matches.group(2)))
    ),
    (
        re.compile(r"jio (a|b), ((?:\+|\-)\d+)"),
        lambda matches: ("JUMP_ONE", matches.group(1), parseJump(matches.group(2)))
    ),
]

def parseFile(contents: str) -> int:
    instructions = []

    for line in contents.splitlines():
        for (pattern, f) in instruction_parsers:
            if match := pattern.match(line):
                instructions.append(f(match))
    
    registers = { 'a': 0, 'b': 0 }
    instruction = 0
    while instruction < len(instructions):
        i = instructions[instruction]
        if i[0] == "HALF":
            (_, register) = i
            registers[register] = int(registers[register] / 2)
            instruction += 1
        elif i[0] == "TRIPLE":
            (_, register) = i
            registers[register] *= 3
            instruction += 1
        elif i[0] == "INCREMENT":
            (_, register) = i
            registers[register] += 1
            instruction += 1
        elif i[0] == "JUMP":
            (_, jump) = i
            instruction += jump
        elif i[0] == "JUMP_EVEN":
            (_, register, jump) = i
            if registers[register] % 2 == 0:
                instruction += jump
            else:
                instruction += 1
        elif i[0] == "JUMP_ONE":
            (_, register, jump) = i
            if registers[register] == 1:
                instruction += jump
            else:
                instruction += 1
        else:
            raise ValueError(i)
    return registers['b']

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    main()
# https://adventofcode.com/2015/day/7
import os
import re

def parseOperation(op):
    if m := re.match(r"^(\d+)$", op):
        return (":=", int(m.group(1)))
    elif m := re.match(r"^NOT (\w+)$", op):
        return ("!", m.group(1))
    elif m := re.match(r"^(\w+)$", op):
        return ("=", m.group(1))
    elif m := re.match(r"^(\w+) (AND|OR) (\w+)$", op):
        return ("&&" if m.group(2) == "AND" else "||", m.group(1), m.group(3))
    elif m := re.match(r"^(\w+) (R|L)SHIFT (\d+)$", op):
        return (">>" if m.group(2) == "R" else "<<", m.group(1), int(m.group(3)))
    else:
        raise ValueError("Ah shit", op)

def parseLine(values, line: str):
    matches = re.match(r"(.*) -> (\w+)", line.strip())
    operation = matches.group(1)
    result = matches.group(2)

    values[result] = parseOperation(operation)

def parseFile(lines: list[str]) -> int:
    values = {}
    for line in lines:
        parseLine(values, line)
    
    state = {}
    def doOperation(variable):
        if variable in state:
            return state[variable]

        try:
            return int(variable)
        except ValueError:
            pass

        operation = values[variable]
        if operation[0] == ':=':
            state[variable] = operation[1]
        elif operation[0] == '=':
            state[variable] = doOperation(operation[1])
        elif operation[0] == '!':
            state[variable] = ~doOperation(operation[1])
        elif operation[0] == '&&':
            state[variable] = doOperation(operation[1]) & doOperation(operation[2])
        elif operation[0] == '||':
            state[variable] = doOperation(operation[1]) | doOperation(operation[2])
        elif operation[0] == '>>':
            state[variable] = doOperation(operation[1]) >> operation[2]
        elif operation[0] == '<<':
            state[variable] = doOperation(operation[1]) << operation[2]
        return state[variable]

    a = doOperation('a')
    state = {"b": a}
    return doOperation('a')

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f))

if __name__ == "__main__":
    main()
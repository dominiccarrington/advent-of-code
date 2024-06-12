# https://adventofcode.com/2015/day/11
import os

INVALID_CHARS = ['i', 'o', 'l']

def incrementPassword(pwd: str) -> str:
    bs = list(bytes(pwd, 'utf-8'))

    i = 0
    while i < len(bs):
        if bs[i] == 105 or bs[i] == 108 or bs[i] == 111:
            bs[i] += 1
            for j in range(i + 1, len(bs)):
                bs[j] = 97
            break
        i += 1

    rbs = list(reversed(bs))
    i = 0
    while True:
        rbs[i] += 1
        if rbs[i] == 105 or rbs[i] == 108 or rbs[i] == 111:
            i += 1
        if rbs[i] >= 123:
            rbs[i] -= 26
            i += 1
        else:
            break
    
    return "".join([chr(c) for c in list(reversed(rbs))])

def validPassword(pwd: str) -> bool:
    for c in INVALID_CHARS:
        if c in pwd:
            return False
    
    found = []
    i = 0
    while i < len(pwd) - 1:
        if pwd[i] not in found and pwd[i] == pwd[i+1]:
            found.append(pwd[i])
            i += 1
        i += 1
    if len(found) < 2:
        return False
    
    for i in range(0, len(pwd) - 3):
        c = ord(pwd[i])
        if c > 121: # aka y,z
            continue

        c2, c3 = chr(c + 1), chr(c + 2)
        if pwd[i + 1] == c2 and pwd[i + 2] == c3:
            return True
    return False

def parseFile(pwd: str) -> str:
    while True:
        pwd = incrementPassword(pwd)
        if validPassword(pwd):
            return pwd


def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(parseFile(f.read().strip())))

if __name__ == "__main__":
    main()
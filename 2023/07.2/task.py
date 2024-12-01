# https://adventofcode.com/2023/day/7
import os

def parseHand(hand: str) -> int:
    if "J" in hand:
        return max([ parseHand(hand.replace("J", c)) for c in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'] ])

    chars = {}
    for c in hand:
        chars[c] = chars.get(c, 0) + 1

    keys = list(chars.keys())

    if len(keys) == 1 and chars[keys[0]] == 5:
        return 6
    elif len(chars.keys()) == 2 and (chars[keys[0]] == 4 or chars[keys[1]] == 4):
        return 5
    elif len(chars.keys()) == 2 and ((chars[keys[0]] == 3 and chars[keys[1]] == 2) or (chars[keys[0]] == 2 and chars[keys[1]] == 3)):
        return 4
    elif len(chars.keys()) == 3 and (any(chars[k] == 3 for k in keys)):
        return 3
    elif len(list(filter(None, [chars[k] == 2 for k in keys]))) == 2:
        return 2
    elif len(list(filter(None, [chars[k] == 2 for k in keys]))) == 1:
        return 1
    else:
        return 0

    return 0

def cardValue(c):
    if c == "A":
        return 14
    elif c == "K":
        return 13
    elif c == "Q":
        return 12
    elif c == "J":
        return 1
    elif c == "T":
        return 10
    else:
        return int(c)

def sorting_func(a):
    (type, hand, _) = a
    return str(type) + ''.join(["{0:0=2d}".format(cardValue(c)) for c in hand])

def parseFile(lines: str):
    hands = []

    for line in lines:
        [hand, wager] = line.strip().split()
        hands.append((parseHand(hand), hand, int(wager)))

    # Low to High
    hands.sort(key=sorting_func)
    
    sigma = 0
    for i in range(len(hands)):
        (_, hand, wager) = hands[i]
        sigma += (wager * (i + 1))
    return sigma


def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.readlines()))

if __name__ == "__main__":
    main();
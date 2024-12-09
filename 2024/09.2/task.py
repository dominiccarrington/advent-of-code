# https://adventofcode.com/2024/day/9
import os
from timeit import timeit

def parseFile(fileContents: str) -> int:
    blocks = []
    for i in range(0, len(fileContents), 2):
        blocks.append({
            "id": int(i / 2),
            "count": int(fileContents[i])
        })

        try:
            blocks.append({
                "id": None,
                "count": int(fileContents[i + 1])
            })
        except IndexError:
            pass
    
    i = len(blocks) - 1
    while i > 0:
        if blocks[i]['id'] is None:
            i -= 1
            continue
        
        for j in range(0, i):
            if blocks[j]['id'] is not None:
                continue
            if blocks[j]['count'] < blocks[i]['count']:
                continue
            
            block = blocks.pop(i)
            blocks.insert(j, block)
            blocks[j + 1]['count'] -= block['count']
            blocks.insert(i, {"id": None, "count": block['count']})
            break
        i -= 1

    while blocks[-1]['id'] is None:
        blocks.pop()

    s = 0
    i = 0
    for block in blocks:
        for _ in range(block['count']):
            s += (block['id'] if block['id'] is not None else 0) * i
            i += 1
    return s

def main():
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        print(parseFile(f.read().strip()))

if __name__ == "__main__":
    time = timeit(main, 'gc.enable()', number=1)
    print(f"Time Taken: {time} secs")
from timeit import repeat
import task
import os

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    with open(dir + '/input.txt') as f:
        contents = f.readlines()
    print(repeat(lambda: task.parseFile(contents), number=1))
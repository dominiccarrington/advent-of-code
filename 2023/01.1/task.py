import os

def convertToInteger(str):
    if len(str) > 1:
        return None
    
    try:
        return int(str)
    except ValueError:
        return None

sigma = 0

dir = os.path.dirname(os.path.relpath(__file__))
with open(dir + '/input.txt') as f:
    for line in f:
        i = 0
        
        first_number = None
        last_number = None
        while i <= len(line) and (first_number is None or last_number is None):
            if first_number is None:
                first_number = convertToInteger(line[i])

            if last_number is None:
                last_number = convertToInteger(line[len(line) - i - 1])

            i += 1
        if first_number is None or last_number is None:
            raise RuntimeError("[{}] first_number ({}) or last_number ({}) are none".format(line, first_number, last_number))

        sigma += (first_number * 10 + last_number)

print(sigma)
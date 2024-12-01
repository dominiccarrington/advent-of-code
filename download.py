import requests
import sys
from bs4 import BeautifulSoup
import os

def download(year, day):
    base_url = f"https://adventofcode.com/{year}/day/{day}"

    day = str(day)
    if len(day) == 1:
        day = "0" + day

    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    descriptions = soup.find_all(class_='day-desc')

    if not os.path.exists(f"{year}/{day}.1"):
        os.makedirs(f"{year}/{day}.1")
        
    if len(descriptions) == 2:
        if not os.path.exists(f"{year}/{day}.2"):
            os.makedirs(f"{year}/{day}.2")

    readme = str(descriptions[0])
    with open(f"{year}/{day}.1/task.md", 'w') as file:
        file.write(readme)

    if len(descriptions) == 2:
        with open(f"{year}/{day}.2/task.md", 'w') as file:
            file.write(str(descriptions[0]) + "\n" + str(descriptions[1]))

    with open( 'session.txt', 'r' ) as session:
        s = requests.Session()
        s.cookies.set("session", session.read())
        input = s.get(base_url + "/input").content

        with open(f"{year}/{day}.1/input.txt", 'wb') as file:
            file.write(input)

        if len(descriptions) == 2:
            with open(f"{year}/{day}.2/input.txt", 'wb') as file:
                file.write(input)

def main():
    if len(sys.argv) < 3:
        print("[year] [day] are required", file=sys.stderr)
        exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    if day == "*":
        for i in range(1, 26):
            print(f"Day {i}...", end="")
            download(year, i)
            print(' Complete')
    else:
        download(year, day)

if __name__ == "__main__":
    main()
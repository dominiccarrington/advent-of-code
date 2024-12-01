from git import Repo
import re
from os.path import exists as file_exists
from bs4 import BeautifulSoup

repo = Repo()
commits = [c for c in repo.iter_commits()]

pattern = re.compile(r"\[(\d{4})\]\[(\d{1,2}).(1|2)\] (Complete|Correct)")
commits_with_puzzle_specified = filter(lambda s: s is not None, [pattern.match(c.message) for c in commits])

years = {year: {day: [False, False] for day in range(1, 26)} for year in range(2015, 2025)}

for matches in commits_with_puzzle_specified:
    year = int(matches.group(1))
    puzzle = int(matches.group(2))
    part = int(matches.group(3))

    years[year][puzzle][part - 1] = True

def create_top_level_table_line(year):
    part1_completed = len([day for day in years[year].values() if day[0]])
    part2_completed = len([day for day in years[year].values() if day[1]])
    parts_completed = part1_completed + part2_completed

    parts_completed_str = f"{parts_completed}/50"
    part1_completed_str = f"{part1_completed}/25"
    part2_completed_str = f"{part2_completed}/25"

    year_line = f"| [{year}](/{year}/README.md) | {parts_completed_str} | {part1_completed_str} | {part2_completed_str} |\n"

    return year_line

def write_year_readme(year):
    if not file_exists(str(year)):
        print("Skipped " + str(year))
        return
    
    days = years[year]

    def generate_link_for_day(day, task):
        ret = ":heavy_check_mark:" if days[day][task-1] else ":x:"
        day_str = str(day) if day >= 10 else f"0{day}"

        if file_exists(f"{year}/{day_str}.{task}"):
            ret += f" [(link)](/{year}/{day_str}.{task})"

        return ret
    README = f"""
# Advent of Code {year}

> [https://adventofcode.com/{year}/](https://adventofcode.com/{year}/)

| Task | Part 1 | Part 2 |
| ---- | ------ | ------ |
"""
    for i in range(1, 26):
        task_str = ""
        i_str = str(i) if i >= 10 else f"0{i}"
        if file_exists(f"{year}/{i_str}.1/README.md"):
            with open(f"{year}/{i_str}.1/README.md", 'r') as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                task_str = str(soup.article.h2.contents[0]).strip(' -')
        else:
            task_str = f"Day {i}"
        
        README += f"| {task_str} | {generate_link_for_day(i, 1)} | {generate_link_for_day(i, 2)} |\n"
    
    with open(f"{year}/README.md", 'w') as f:
        f.write(README.strip())
    
    repo.index.add(f"{year}/README.md")

README = """
# Advent of Code

> [https://adventofcode.com/](https://adventofcode.com/)

| Year          | Completed Tasks | Completed Part 1 | Completed Part 2 |
| ------------- | --------------- | ---------------- | ---------------- |
"""

for year in years.keys():
    write_year_readme(year)
    README += create_top_level_table_line(year)

with open('README.md', 'w') as f:
    f.write(README.strip())

repo.index.add('README.md')
repo.index.commit('chore: Update README')
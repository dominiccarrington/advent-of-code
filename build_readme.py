from git import Repo
import re

repo = Repo()
commits = [c for c in repo.iter_commits('main')]

pattern = re.compile(r"\[(\d{4})\]\[(\d{1,2}).(1|2)\] (Complete|Correct)")
commits_with_puzzle_specified = filter(lambda s: s is not None, [pattern.match(c.message) for c in commits])

years = {year: {day: [False, False] for day in range(1, 26)} for year in range(2015, 2024)}

for matches in commits_with_puzzle_specified:
    year = int(matches.group(1))
    puzzle = int(matches.group(2))
    part = int(matches.group(3))

    years[year][puzzle][part - 1] = True

README = """
# Advent of Code

> [https://adventofcode.com/](https://adventofcode.com/)

| Year          | Completed Tasks | Completed Part 1 | Completed Part 2 |
| ------------- | --------------- | ---------------- | ---------------- |
"""

def create_top_level_table_line(year):
    column_len = [len("Completed Tasks"), len("Completed Part 1"), len("Completed Part 2")]

    part1_completed = len([day for day in years[year].values() if day[0]])
    part2_completed = len([day for day in years[year].values() if day[1]])
    parts_completed = part1_completed + part2_completed

    parts_completed_str = f"{parts_completed}/50"
    parts_completed_str += " " * (column_len[0] - len(parts_completed_str))
    part1_completed_str = f"{part1_completed}/25"
    part1_completed_str += " " * (column_len[1] - len(part1_completed_str))
    part2_completed_str = f"{part2_completed}/25"
    part2_completed_str += " " * (column_len[2] - len(part2_completed_str))

    year_line = f"| [{year}](/{year}) | {parts_completed_str} | {part1_completed_str} | {part2_completed_str} |\n"

    return year_line

for year in years.keys():
    README += create_top_level_table_line(year)

with open('README.md', 'w') as f:
    f.write(README.strip())

repo.index.add('README.md')
repo.index.commit('chore: Update README')
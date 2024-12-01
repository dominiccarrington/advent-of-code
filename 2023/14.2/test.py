import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().split("\n")
            ),
            64
        )
    
    def test_cycle(self):
        input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().splitlines()
        lines = [list(line.strip()) for line in input]

        cycle = task.doCycle(lines)
        output = "\n".join(["".join(a) for a in cycle])
        self.assertEqual(
            output,
"""
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
""".strip()
        )


if __name__ == "__main__":
    unittest.main();
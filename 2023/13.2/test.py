import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip()
            ),
            400
        )

class GridTest(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            task.parseGrid(
"""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
""".strip().split("\n")
            ),
            300
        )
    def test_example2(self):
        self.assertEqual(
            task.parseGrid(
"""
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip().split("\n")
            ),
            100
        )

if __name__ == "__main__":
    unittest.main();
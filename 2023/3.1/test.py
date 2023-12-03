import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().split("\n")
            ),
            4361
        )

if __name__ == "__main__":
    unittest.main();
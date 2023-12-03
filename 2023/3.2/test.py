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
            467835
        )

class FindNumberTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(
            task.findNumber("1234", 0),
            1234
        )
    def test_1(self):
        self.assertEqual(
            task.findNumber("1234", 1),
            1234
        )
    def test_2(self):
        self.assertEqual(
            task.findNumber("1234", 2),
            1234
        )
    def test_3(self):
        self.assertEqual(
            task.findNumber("1234", 3),
            1234
        )

if __name__ == "__main__":
    unittest.main();
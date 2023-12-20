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
    def test_all_the_corners(self):
        self.assertEqual(
            task.parseFile(
"""
11.13
..%..
17.19
""".strip().split("\n")
            ),
            60
        )
    def test_all_the_cardinals(self):
        self.assertEqual(
            task.parseFile(
"""
...101...
.103%107.
...109...
""".strip().split("\n")
            ),
            420
        )

class FindNumberTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(
            task.findNumber("1234.5678", 0),
            1234
        )
    def test_1(self):
        self.assertEqual(
            task.findNumber("1234.5678", 1),
            1234
        )
    def test_2(self):
        self.assertEqual(
            task.findNumber("1234.5678", 2),
            1234
        )
    def test_3(self):
        self.assertEqual(
            task.findNumber("1234.5678", 3),
            1234
        )
    def test_5(self):
        self.assertEqual(
            task.findNumber("1234.5678", 5),
            5678
        )
    def test_6(self):
        self.assertEqual(
            task.findNumber("1234.5678", 6),
            5678
        )
    def test_7(self):
        self.assertEqual(
            task.findNumber("1234.5678", 7),
            5678
        )
    def test_8(self):
        self.assertEqual(
            task.findNumber("1234.5678", 8),
            5678
        )

if __name__ == "__main__":
    unittest.main();
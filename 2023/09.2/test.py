import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().split("\n")
            ),
            2
        )
class ListTest(unittest.TestCase):
    def test_line1(self):
        self.assertEqual(task.parseLine("0 3 6 9 12 15"), -3)

    def test_line2(self):
        self.assertEqual(task.parseLine("1 3 6 10 15 21"), 0)

    def test_line3(self):
        self.assertEqual(task.parseLine("10 13 16 21 30 45"), 5)

if __name__ == "__main__":
    unittest.main();
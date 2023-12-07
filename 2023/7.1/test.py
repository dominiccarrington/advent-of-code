import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().split("\n")
            ),
            6440
        )

class ParseHandTest(unittest.TestCase):
    def test_JK949(self):
        self.assertEqual(
            task.parseHand("JK949"),
            1
        )

class SortingTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            task.sorting_func((2, "12345", None)),
            "20102030405"
        )
    def test_2(self):
        self.assertEqual(
            task.sorting_func((6, "AKQJT", None)),
            "61413121110"
        )

if __name__ == "__main__":
    unittest.main();
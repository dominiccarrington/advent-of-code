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
            5905
        )

class ParseHandTest(unittest.TestCase):
    def test_KKKKK(self):
        self.assertEqual(
            task.parseHand("KKKKK"),
            6
        )
    def test_JJKKK(self):
        self.assertEqual(
            task.parseHand("JJKKK"),
            6
        )
    def test_JJJJJ(self):
        self.assertEqual(
            task.parseHand("JJJJJ"),
            6
        )
    def test_KKJJQ(self):
        self.assertEqual(
            task.parseHand("KKJJQ"),
            5
        )
    def test_JK949(self):
        self.assertEqual(
            task.parseHand("JK949"),
            3
        )
    def test_1234J(self):
        self.assertEqual(
            task.parseHand("1234J"),
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
            "61413120110"
        )

if __name__ == "__main__":
    unittest.main();
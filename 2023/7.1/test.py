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


if __name__ == "__main__":
    unittest.main();
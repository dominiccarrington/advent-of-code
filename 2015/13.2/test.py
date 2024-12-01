import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine("Alice would gain 54 happiness units by sitting next to Bob."),
            ("Alice", "Bob", 54)
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine("Alice would lose 79 happiness units by sitting next to Carol."),
            ("Alice", "Carol", -79)
        )

if __name__ == '__main__':
    unittest.main()
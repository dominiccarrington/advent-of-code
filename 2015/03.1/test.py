import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine(">"),
            2
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine("^>v<"),
            4
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine("^v^v^v^v^v"),
            2
        )

if __name__ == '__main__':
    unittest.main()
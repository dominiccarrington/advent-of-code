import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine("^v"),
            3
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine("^>v<"),
            3
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine("^v^v^v^v^v"),
            11
        )

if __name__ == '__main__':
    unittest.main()
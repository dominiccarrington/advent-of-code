import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine("2x3x4"),
            34
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine("1x1x10"),
            14
        )

if __name__ == '__main__':
    unittest.main()
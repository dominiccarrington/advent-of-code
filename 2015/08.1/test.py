import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine('""'),
            0
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine('"abc"'),
            3
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine('"aaa\"aaa"'),
            7
        )
    def test_d(self):
        self.assertEqual(
            task.parseLine('"\\x27"'),
            1
        )

if __name__ == '__main__':
    unittest.main()
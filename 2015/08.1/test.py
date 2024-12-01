import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine('""'),
            2
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine('"abc"'),
            2
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine('"aaa\"aaa"'),
            2
        )
    def test_d(self):
        self.assertEqual(
            task.parseLine('"\\x27"'),
            5
        )

if __name__ == '__main__':
    unittest.main()
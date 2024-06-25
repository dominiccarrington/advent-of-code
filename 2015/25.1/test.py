import task
import unittest

class SequenceTestSuite(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            [1, 2, 4, 7, 11, 16, 22],
            [task.sequence(i) for i in range(1, 8)]
        )

class TestSuite(unittest.TestCase):
    def test_2_1(self):
        self.assertEqual(
            31916031,
            task.calculateValue(2, 1)
        )
    def test_5_1(self):
        self.assertEqual(
            77061,
            task.calculateValue(5, 1)
        )

if __name__ == '__main__':
    unittest.main()
import task
import unittest

class SequenceTestSuite(unittest.TestCase):
    def test_column_1(self):
        self.assertEqual(
            [1, 2, 4, 7, 11, 16, 22],
            [task.sequence_down_col_1(i) for i in range(1, 8)]
        )
    def test_row_1(self):
        self.assertEqual(
            [1, 3, 6, 10, 15, 21],
            [task.sequence_across_row_1(i) for i in range(1, 7)]
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
    def test_3_2(self):
        self.assertEqual(
            8057251,
            task.calculateValue(3, 2)
        )

if __name__ == '__main__':
    unittest.main()
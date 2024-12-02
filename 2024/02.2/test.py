import task
import unittest

class ParseLineTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine('7 6 4 2 1'),
            True
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine('1 2 7 8 9'),
            False
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine('9 7 6 2 1'),
            False
        )
    def test_d(self):
        self.assertEqual(
            task.parseLine('1 3 2 4 5'),
            True
        )
    def test_e(self):
        self.assertEqual(
            task.parseLine('8 6 4 4 1'),
            True
        )
    def test_f(self):
        self.assertEqual(
            task.parseLine('1 3 6 7 9'),
            True
        )
    def test_g(self):
        self.assertEqual(
            task.parseLine('9 13 8 7 6 5'),
            True
        )
    def test_h(self):
        self.assertEqual(
            task.parseLine('9 10 8 7 6 5'),
            True
        )

if __name__ == '__main__':
    unittest.main()
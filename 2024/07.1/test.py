import task
import unittest

class ParseLineTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine('190: 10 19'), 190
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine('3267: 81 40 27'), 3267
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine('83: 17 5'), 0
        )
    def test_d(self):
        self.assertEqual(
            task.parseLine('156: 15 6'), 0
        )
    def test_e(self):
        self.assertEqual(
            task.parseLine('7290: 6 8 6 15'), 0
        )
    def test_f(self):
        self.assertEqual(
            task.parseLine('161011: 16 10 13'), 0
        )
    def test_g(self):
        self.assertEqual(
            task.parseLine('192: 17 8 14'), 0
        )
    def test_h(self):
        self.assertEqual(
            task.parseLine('21037: 9 7 18 13'), 0
        )
    def test_i(self):
        self.assertEqual(
            task.parseLine('292: 11 6 16 20'), 292
        )

if __name__ == '__main__':
    unittest.main()
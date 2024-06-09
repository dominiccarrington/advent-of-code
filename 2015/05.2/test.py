import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine("qjhvhtzxzqqjkmpb"),
            1
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine("xxyxx"),
            1
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine("uurcxstgmygtbstg"),
            0
        )
    def test_d(self):
        self.assertEqual(
            task.parseLine("ieodomkazucvgmuy"),
            0
        )


if __name__ == '__main__':
    unittest.main()
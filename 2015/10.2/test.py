import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.createNewSequence("1"),
            "11"
        )
    def test_b(self):
        self.assertEqual(
            task.createNewSequence("11"),
            "21"
        )
    def test_c(self):
        self.assertEqual(
            task.createNewSequence("21"),
            "1211"
        )
    def test_d(self):
        self.assertEqual(
            task.createNewSequence("1211"),
            "111221"
        )
    def test_e(self):
        self.assertEqual(
            task.createNewSequence("111221"),
            "312211"
        )

if __name__ == '__main__':
    unittest.main()
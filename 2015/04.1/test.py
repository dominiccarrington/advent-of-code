import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("abcdef"),
            609043
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("pqrstuv"),
            1048970
        )

if __name__ == '__main__':
    unittest.main()
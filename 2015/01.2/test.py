import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile(")"),
            1
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("()())"),
            5
        )

if __name__ == '__main__':
    unittest.main()
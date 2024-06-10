import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine('""'),
            4
        )

if __name__ == '__main__':
    unittest.main()
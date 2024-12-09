import task
import unittest

class ParseFileTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("2333133121414131402".strip()), 2858
        )

if __name__ == '__main__':
    unittest.main()
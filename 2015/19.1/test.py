import task
import unittest

class TestSuite(unittest.TestCase):
    def test_example(self):
        INPUT = """
H => HO
H => OH
O => HH

HOHOHO
""".strip()
        self.assertEqual(
            task.parseFile(INPUT),
            7
        )


if __name__ == '__main__':
    unittest.main()
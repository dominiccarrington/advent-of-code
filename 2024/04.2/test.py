import task
import unittest

class ParseFileTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("""
M.S
.A.
M.S
""".strip()), 1
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("""
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip()), 9
        )

if __name__ == '__main__':
    unittest.main()
import task
import unittest

class ParseFileTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("""
..X...
.SAMX.
.A..A.
XMAS.S
.X....
""".strip()), 4
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()), 18
        )

if __name__ == '__main__':
    unittest.main()
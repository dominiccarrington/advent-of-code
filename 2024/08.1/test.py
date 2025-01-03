import task
import unittest

class ParseFileTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()), 14
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("""
..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
..........
""".strip()), 2
        )
    def test_c(self):
        self.assertEqual(
            task.parseFile("""
..........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
..........
""".strip()), 4
        )

if __name__ == '__main__':
    unittest.main()
import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip().split()
            ),
            4
        )
    def test_example2(self):
        self.assertEqual(
            task.parseFile(
"""
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
...........
""".strip().split()
            ),
            4
        )
    def test_example3(self):
        self.assertEqual(
            task.parseFile(
"""
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip().split()
            ),
            8
        )
    def test_example4(self):
        self.assertEqual(
            task.parseFile(
"""
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip().split()
            ),
            10
        )

class PointsIntoTest(unittest.TestCase):
    def test_ns(self):
        self.assertTrue(
            task.pointsInto("|", (1, 1), (2, 1))
        )
        self.assertTrue(
            task.pointsInto("|", (1, 1), (0, 1))
        )
    def test_ew(self):
        self.assertTrue(
            task.pointsInto("-", (1, 1), (1, 2))
        )
        self.assertTrue(
            task.pointsInto("-", (1, 1), (1, 0))
        )
    def test_ne(self):
        self.assertTrue(
            task.pointsInto("L", (1, 1), (0, 1))
        )
        self.assertTrue(
            task.pointsInto("L", (1, 1), (1, 2))
        )
    def test_nw(self):
        self.assertTrue(
            task.pointsInto("J", (1, 1), (0, 1))
        )
        self.assertTrue(
            task.pointsInto("J", (1, 1), (1, 0))
        )
    def test_sw(self):
        self.assertTrue(
            task.pointsInto("7", (1, 1), (1, 0))
        )
        self.assertTrue(
            task.pointsInto("7", (1, 1), (2, 1))
        )
    def test_se(self):
        self.assertTrue(
            task.pointsInto("F", (1, 1), (2, 1))
        )
        self.assertTrue(
            task.pointsInto("F", (1, 1), (1, 2))
        )

if __name__ == "__main__":
    unittest.main();
import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip().split()
            ),
            8
        )
    def test_example2(self):
        self.assertEqual(
            task.parseFile(
"""
.....
.S-7.
.|.|.
.L-J.
.....
""".strip().split()
            ),
            4
        )
    def test_example3(self):
        self.assertEqual(
            task.parseFile(
"""
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip().split()
            ),
            8
        )
    def test_example4(self):
        self.assertEqual(
            task.parseFile(
"""
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
""".strip().split()
            ),
            4
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
import task
import unittest

class FindGaurdTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.findGuard([
                '....#.....', 
                '.........#', 
                '..........', 
                '..#.......', 
                '.......#..', 
                '..........', 
                '.#..^.....', 
                '........#.', 
                '#.........', 
                '......#...', 
            ]), (6, 4, 0)
        )
    def test_b(self):
        self.assertEqual(
            task.findGuard([
                '....#.....', 
                '.........#', 
                '..........', 
                '..#.......', 
                '.......#..', 
                '..........', 
                '.#..>.....', 
                '........#.', 
                '#.........', 
                '......#...', 
            ]), (6, 4, 1)
        )
    def test_c(self):
        self.assertEqual(
            task.findGuard([
                '....#.....', 
                '.........#', 
                '..........', 
                '..#.......', 
                '.......#..', 
                '..........', 
                '.#..v.....', 
                '........#.', 
                '#.........', 
                '......#...', 
            ]), (6, 4, 2)
        )
    def test_d(self):
        self.assertEqual(
            task.findGuard([
                '....#.....', 
                '.........#', 
                '..........', 
                '..#.......', 
                '.......#..', 
                '..........', 
                '.#..<.....', 
                '........#.', 
                '#.........', 
                '......#...', 
            ]), (6, 4, 3)
        )

class ParseFileTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile('''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''.strip()), 41
        )

if __name__ == '__main__':
    unittest.main()
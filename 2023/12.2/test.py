import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().split("\n")
            ),
            525152
        )

class LineTest(unittest.TestCase):
    def test_line1(self):
        self.assertEqual(
            task.parseLine("???.### 1,1,3"),
            1
        )
    def test_line2(self):
        self.assertEqual(
            task.parseLine(".??..??...?##. 1,1,3"),
            16384
        )
    def test_line3(self):
        self.assertEqual(
            task.parseLine("?#?#?#?#?#?#?#? 1,3,1,6"),
            1
        )
    def test_line4(self):
        self.assertEqual(
            task.parseLine("????.#...#... 4,1,1"),
            16
        )
    def test_line5(self):
        self.assertEqual(
            task.parseLine("????.######..#####. 1,6,5"),
            2500
        )
    def test_line6(self):
        self.assertEqual(
            task.parseLine("?###???????? 3,2,1"),
            506250
        )

if __name__ == "__main__":
    unittest.main();
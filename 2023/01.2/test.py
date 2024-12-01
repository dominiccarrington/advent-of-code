import task
import unittest

class ConvertLineToNumber(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.convertLineToNumber("two1nine"),
            29
        )
    def test_b(self):
        self.assertEqual(
            task.convertLineToNumber("eightwothree"),
            83
        )
    def test_c(self):
        self.assertEqual(
            task.convertLineToNumber("abcone2threexyz"),
            13
        )
    def test_d(self):
        self.assertEqual(
            task.convertLineToNumber("xtwone3four"),
            24
        )
    def test_e(self):
        self.assertEqual(
            task.convertLineToNumber("4nineeightseven2"),
            42
        )
    def test_f(self):
        self.assertEqual(
            task.convertLineToNumber("zoneight234"),
            14
        )
    def test_g(self):
        self.assertEqual(
            task.convertLineToNumber("7pqrstsixteen"),
            76
        )
    # https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
    def test_h(self):
        self.assertEqual(
            task.convertLineToNumber("eighthree"),
            83
        )
    # https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
    def test_i(self):
        self.assertEqual(
            task.convertLineToNumber("sevenine"),
            79
        )

if __name__ == '__main__':
    unittest.main()
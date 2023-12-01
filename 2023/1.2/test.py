import task
import unittest

class ConvertToIntegerTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task.convertToInteger("1"), 1)
    def test_2(self):
        self.assertEqual(task.convertToInteger("2"), 2)
    def test_3(self):
        self.assertEqual(task.convertToInteger("3"), 3)
    def test_4(self):
        self.assertEqual(task.convertToInteger("4"), 4)
    def test_5(self):
        self.assertEqual(task.convertToInteger("5"), 5)
    def test_6(self):
        self.assertEqual(task.convertToInteger("6"), 6)
    def test_7(self):
        self.assertEqual(task.convertToInteger("7"), 7)
    def test_8(self):
        self.assertEqual(task.convertToInteger("8"), 8)
    def test_9(self):
        self.assertEqual(task.convertToInteger("9"), 9)
    def test_0(self):
        self.assertIsNone(task.convertToInteger("0"))
    def test_a(self):
        self.assertIsNone(task.convertToInteger("a"))

class ReplaceNumericWithInteger(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.replaceNumericWithInteger("three9three"),
            "393"
        )
    def test_b(self):
        self.assertEqual(
            task.replaceNumericWithInteger("5hxseven7jhsqlsftml"),
            "5hx77jhsqlsftml"
        )
    def test_c(self):
        self.assertEqual(
            task.replaceNumericWithInteger("xtwone3four"),
            "x2ne34",
        )

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
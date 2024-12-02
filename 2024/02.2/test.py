import bruteforce as task
import unittest

# Extra test cases found on: https://www.reddit.com/r/adventofcode/comments/1h4shdu/2024_day_2_part2_edge_case_finder/

class ParseLineTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseLine("7 6 4 2 1"), True
        )
    def test_b(self):
        self.assertEqual(
            task.parseLine("1 2 7 8 9"), False
        )
    def test_c(self):
        self.assertEqual(
            task.parseLine("9 7 6 2 1"), False
        )
    def test_d(self):
        self.assertEqual(
            task.parseLine("1 3 2 4 5"), True
        )
    def test_e(self):
        self.assertEqual(
            task.parseLine("8 6 4 4 1"), True
        )
    def test_f(self):
        self.assertEqual(
            task.parseLine("1 3 6 7 9"), True
        )
    def test_PhilmacFLy_a(self):
        self.assertEqual(
            task.parseLine("48 46 47 49 51 54 56"), True
        )
    def test_PhilmacFLy_b(self):
        self.assertEqual(
            task.parseLine("1 1 2 3 4 5"), True
        )
    def test_PhilmacFLy_c(self):
        self.assertEqual(
            task.parseLine("1 2 3 4 5 5"), True
        )
    def test_PhilmacFLy_d(self):
        self.assertEqual(
            task.parseLine("5 1 2 3 4 5"), True
        )
    def test_PhilmacFLy_e(self):
        self.assertEqual(
            task.parseLine("1 4 3 2 1"), True
        )
    def test_PhilmacFLy_f(self):
        self.assertEqual(
            task.parseLine("1 6 7 8 9"), True
        )
    def test_PhilmacFLy_g(self):
        self.assertEqual(
            task.parseLine("1 2 3 4 3"), True
        )
    def test_PhilmacFLy_h(self):
        self.assertEqual(
            task.parseLine("9 8 7 6 7"), True
        )
    def test_PhilmacFLy_i(self):
        self.assertEqual(
            task.parseLine("7 10 8 10 11"), True
        )
    def test_PhilmacFLy_j(self):
        self.assertEqual(
            task.parseLine("29 28 27 25 26 25 22 20"), True
        )
    def test_Tsanawo_a(self):
        self.assertEqual(
            task.parseLine("9 8 7 7 7"), False
        )
    def test_Glueckskeks4_a(self):
        self.assertEqual(
            task.parseLine("1 1 1 1"), False
        )
    def test_i(self):
        self.assertEqual(
            task.parseLine('9 10 8 7 9 6'),
            False
        )
    def test_j(self):
        self.assertEqual(
            task.parseLine('1 2 3 4 2 3 6 7'),
            False
        )
    def test_k(self):
        self.assertEqual(
            task.parseLine('7 6 3 2 4 3 2 1'),
            False
        )

    def test_aadi_ctive_a(self):
        self.assertEqual(
            task.parseLine("90 89 86 84 83 79"), True
        )
    def test_aadi_ctive_b(self):
        self.assertEqual(
            task.parseLine("97 96 93 91 85"), True
        )
    def test_aadi_ctive_c(self):
        self.assertEqual(
            task.parseLine("29 26 24 25 21"), True
        )
    def test_aadi_ctive_d(self):
        self.assertEqual(
            task.parseLine("36 37 40 43 47"), True
        )
    def test_aadi_ctive_e(self):
        self.assertEqual(
            task.parseLine("43 44 47 48 49 54"), True
        )
    def test_aadi_ctive_f(self):
        self.assertEqual(
            task.parseLine("35 33 31 29 27 25 22 18"), True
        )
    def test_aadi_ctive_g(self):
        self.assertEqual(
            task.parseLine("77 76 73 70 64"), True
        )
    def test_aadi_ctive_h(self):
        self.assertEqual(
            task.parseLine("68 65 69 72 74 77 80 83"), True
        )
    def test_aadi_ctive_i(self):
        self.assertEqual(
            task.parseLine("37 40 42 43 44 47 51"), True
        )
    def test_aadi_ctive_j(self):
        self.assertEqual(
            task.parseLine("70 73 76 79 86"), True
        )
    def test_pitva90cz_a(self):
        self.assertEqual(
            task.parseLine("31 34 32 30 28 27 24 22"), True
        )
    def test_tiran818_a(self):
        self.assertEqual(
            task.parseLine("75 77 72 70 69"), True
        )
    def test_bluegaspode_a(self):
        self.assertEqual(
            task.parseLine("7 10 8 10 11"), True
        )
    
if __name__ == '__main__':
    unittest.main()
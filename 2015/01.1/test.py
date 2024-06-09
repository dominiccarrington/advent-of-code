import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("(())"),
            0
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("()()"),
            0
        )
    def test_c(self):
        self.assertEqual(
            task.parseFile("((("),
            3
        )
    def test_d(self):
        self.assertEqual(
            task.parseFile("(()(()("),
            3
        )
    def test_e(self):
        self.assertEqual(
            task.parseFile("))((((("),
            3
        )
    def test_f(self):
        self.assertEqual(
            task.parseFile("())"),
            -1
        )
    def test_g(self):
        self.assertEqual(
            task.parseFile("))("),
            -1
        )
    def test_h(self):
        self.assertEqual(
            task.parseFile(")))"),
            -3
        )
    def test_i(self):
        self.assertEqual(
            task.parseFile(")())())"),
            -3
        )

if __name__ == '__main__':
    unittest.main()
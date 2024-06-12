import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            task.parseFile("[1,2,3]"),
            6
        )
    def test_b(self):
        self.assertEqual(
            task.parseFile("""[1,{"c":"red","b":2},3]"""),
            4
        )
    def test_c(self):
        self.assertEqual(
            task.parseFile("""{"d":"red","e":[1,2,3,4],"f":5}"""),
            0
        )
    def test_d(self):
        self.assertEqual(
            task.parseFile("""[1, "red", 5]"""),
            6
        )

if __name__ == '__main__':
    unittest.main()
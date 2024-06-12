import task
import unittest

class IncrementPassword(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
            task.incrementPassword("aaa"),
            "aab"
        )
    def test_wrap(self):
        self.assertEqual(
            task.incrementPassword("aaz"),
            "aba"
        )
    def test_2wrap(self):
        self.assertEqual(
            task.incrementPassword("azz"),
            "baa"
        )
    def test_example_1(self):
        self.assertEqual(
            task.parseFile("abcdefgh"),
            "abcdffaa"
        )
    def test_example_2(self):
        self.assertEqual(
            task.parseFile("ghijklmn"),
            "ghjaabcc"
        )

class TestSuite(unittest.TestCase):
    def test_invalid_2(self):
        self.assertEqual(
            task.validPassword("hijklmmn"),
            False
        )
    def test_invalid_1(self):
        self.assertEqual(
            task.validPassword("abbceffg"),
            False
        )
    def test_invalid_3(self):
        self.assertEqual(
            task.validPassword("abbcegjk"),
            False
        )
    def test_valid(self):
        self.assertEqual(
            task.validPassword("abcdffaa"),
            True
        )
    

if __name__ == '__main__':
    unittest.main()
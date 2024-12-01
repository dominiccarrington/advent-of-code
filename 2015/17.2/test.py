import task
import unittest

class TestSuite(unittest.TestCase):
    def test_a(self):
        task.AMOUNT_OF_EGGNOG = 25
        self.assertEqual(
            task.parseFile("20\n15\n10\n5\n5"),
            4
        )

if __name__ == '__main__':
    unittest.main()
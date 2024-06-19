import task
import unittest

class PrimeFactors(unittest.TestCase):
    def test_15(self):
        self.assertEqual(
            task.primeFactors(15),
            [3, 5]
        )
    def test_64(self):
        self.assertEqual(
            task.primeFactors(64),
            [2, 2, 2, 2, 2, 2]
        )
    def test_221(self):
        self.assertEqual(
            task.primeFactors(221),
            [13, 17]
        )

class PresentsForHouse(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            task.presentsForHouse(1),
            10
        )
    def test_2(self):
        self.assertEqual(
            task.presentsForHouse(2),
            30
        )
    def test_3(self):
        self.assertEqual(
            task.presentsForHouse(3),
            40
        )
    def test_9(self):
        self.assertEqual(
            task.presentsForHouse(9),
            130
        )

class TestSuite(unittest.TestCase):
    def test_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
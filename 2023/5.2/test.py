import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            task.parseSeedRange((1, 1)),
            2048657150
        )
    def test_2(self):
        self.assertEqual(
            task.parseSeedRange((1, 2)),
            2048657150
        )

if __name__ == "__main__":
    unittest.main();
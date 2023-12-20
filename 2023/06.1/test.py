import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
"""
""".strip().split("\n")
            ),
            13
        )


if __name__ == "__main__":
    unittest.main();
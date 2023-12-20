import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_79(self):
        self.assertEqual(
            task.parseFile("test_inputs/seed-to-soil.txt", 79),
            81
        )
    def test_14(self):
        self.assertEqual(
            task.parseFile("test_inputs/seed-to-soil.txt", 14),
            14
        )
    def test_52(self):
        self.assertEqual(
            task.parseFile("test_inputs/seed-to-soil.txt", 52),
            54
        )
    def test_53(self):
        self.assertEqual(
            task.parseFile("test_inputs/seed-to-soil.txt", 53),
            55
        )
    def test_55(self):
        self.assertEqual(
            task.parseFile("test_inputs/seed-to-soil.txt", 55),
            57
        )
    def test_13(self):
        self.assertEqual(
            task.parseFile("test_inputs/seed-to-soil.txt", 13),
            13
        ) 

if __name__ == "__main__":
    unittest.main();
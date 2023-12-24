import task
import unittest

class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
                "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
            ),
            1320
        )

class HashTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.hash("HASH"),
            52
        )

if __name__ == "__main__":
    unittest.main();
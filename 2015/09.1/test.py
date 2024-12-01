import task
import unittest

class TestSuite(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            task.parseFile(
                """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
                """.strip(),
            ),
            605
        )

if __name__ == '__main__':
    unittest.main()
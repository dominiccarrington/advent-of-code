import task
import unittest

STEPS = [
    [
        ".#.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####..",
    ],
    [
        "..##..",
        "..##.#",
        "...##.",
        "......",
        "#.....",
        "#.##..",
    ],
    [
        "..###.",
        "......",
        "..###.",
        "......",
        ".#....",
        ".#....",
    ],
    [
        "...#..",
        "......",
        "...#..",
        "..##..",
        "......",
        "......",
    ],
]

class TestSuite(unittest.TestCase):
    def test_a(self):
        INPUT = STEPS[0]
        EXPECTED_OUTPUT = STEPS[1]

        output = task.doTick(INPUT)
        for i in range(0, len(output)):
            self.assertEqual(output[i], EXPECTED_OUTPUT[i])

    def test_b(self):
        INPUT = STEPS[0]
        EXPECTED_OUTPUT = STEPS[2]

        output = task.doTick(INPUT)
        output = task.doTick(output)
        for i in range(0, len(output)):
            self.assertEqual(output[i], EXPECTED_OUTPUT[i])

if __name__ == '__main__':
    unittest.main()
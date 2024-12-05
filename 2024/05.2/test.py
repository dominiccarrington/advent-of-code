import task
import unittest

# class ParseFileTest(unittest.TestCase):
#     def test_a(self):
#         self.assertEqual(
#             task.parseFile(
# """
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.strip()
#             ), 123
#         )

class FixOrderTest(unittest.TestCase):
    def setUp(self):
        orderingRules = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13""".strip()
        task.orderingRules = {}
        for line in orderingRules.splitlines():
            task.parseOrderingRule(line)
    
    def test_a(self):
        self.assertEqual(
            task.fixOrder([75,97,47,61,53]), [97,75,47,61,53]
        )
    def test_b(self):
        self.assertEqual(
            task.fixOrder([61,13,29]), [61,29,13]
        )
    def test_c(self):
        self.assertEqual(
            task.fixOrder([97,13,75,29,47]), [97,75,47,29,13]
        )

if __name__ == '__main__':
    unittest.main()
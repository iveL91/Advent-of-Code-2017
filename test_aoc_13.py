"""test_aoc_13"""

import unittest
from libs.aoc_13_lib import data_input, part_1, part_2


class TestAoC13(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data = data_input("data/aoc_13_data_test.txt")
        self.assertEqual(part_1(data), 24)

    def test_part_2(self):
        """"""
        data = data_input("data/aoc_13_data_test.txt")
        self.assertEqual(part_2(data), 10)


if __name__ == '__main__':
    unittest.main()

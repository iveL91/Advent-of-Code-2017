"""
    aoc_22
    https://adventofcode.com/2017/day/22
"""

import copy
from typing import List
from libs.aoc_22_lib import data_input, part_1, part_2


def main() -> None:
    start_field, start_position = data_input("data/aoc_22_data.txt")
    start_orientation: List[int] = [-1, 0]

    # Part 1
    p_1 = part_1(copy.deepcopy(start_field), start_position, start_orientation)
    print(f"Part 1: {p_1} is {p_1 == 5266}")

    # Part 2
    p_2 = part_2(start_field, start_position, start_orientation)
    print(f"Part 2: {p_2} is {p_2 == 2511895}")


if __name__ == "__main__":
    main()

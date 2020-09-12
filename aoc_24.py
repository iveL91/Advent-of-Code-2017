"""
    aoc_24
    https://adventofcode.com/2017/day/24
"""

from libs.aoc_24_lib import data_input, part_1, part_2


def main() -> None:
    rest_list = data_input("data/aoc_24_data.txt")

    # Part 1
    p_1 = part_1(rest_list)
    print(f"Part 1: {p_1} is {p_1 == 1511}")

    # Part 2
    p_2 = part_2(rest_list)
    print(f"Part 2: {p_2} is {p_2 == 1471}")


if __name__ == "__main__":
    main()

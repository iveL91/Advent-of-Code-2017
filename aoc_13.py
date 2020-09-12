"""
    aoc_13
    https://adventofcode.com/2017/day/13
"""

from libs.aoc_13_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_13_data.txt")

    # Part 1
    p_1 = part_1(data)
    print(f"Part 1: {p_1} is {p_1 == 1840}")

    # Part 2
    p_2 = part_2(data)
    print(f"Part 2: {p_2} is {p_2 == 3850260}")


if __name__ == "__main__":
    main()

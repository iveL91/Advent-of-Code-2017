"""
    aoc_09
    https://adventofcode.com/2017/day/9
"""

from libs.aoc_09_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_09_data.txt")

    # Part 1
    p_1 = part_1(data)
    print(f"Part 1: {p_1} is {p_1 == 11846}")

    # Part 2
    p_2 = part_2(data)
    print(f"Part 2: {p_2} is {p_2 == 6285}")


if __name__ == "__main__":
    main()

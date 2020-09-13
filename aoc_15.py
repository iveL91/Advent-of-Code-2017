"""
    aoc_15
    https://adventofcode.com/2017/day/15
"""

from libs.aoc_15_lib import data_input, part_1, part_2


def main() -> None:
    starts = data_input("data/aoc_15_data.txt")

    # Part 1
    p_1 = part_1(starts)
    print(f"Part 1: {p_1} is {p_1 == 592}")

    # Part 2
    p_2 = part_2(starts)
    print(f"Part 2: {p_2} is {p_2 == 320}")


if __name__ == "__main__":
    main()

"""
    aoc_14
    https://adventofcode.com/2017/day/14
"""

from libs.aoc_14_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_14_data.txt")
    grid_size: int = 128

    # Part 1
    p_1 = part_1(data, grid_size)
    print(f"Part 1: {p_1} is {p_1 == 8226}")

    # Part 2
    p_2 = part_2(data, grid_size)
    print(f"Part 2: {p_2} is {p_2 == 1128}")


if __name__ == "__main__":
    main()

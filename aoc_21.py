"""
    aoc_21
    https://adventofcode.com/2017/day/21
"""

from libs.aoc_21_lib import data_input, part_1, part_2


def main() -> None:
    instructions_in_out = data_input("data/aoc_21_data.txt")

    # Part 1
    p_1 = part_1(instructions_in_out)
    print(f"Part 1: {p_1} is {p_1 == 150}")

    # Part 2
    p_2 = part_2(instructions_in_out)
    print(f"Part 2: {p_2} is {p_2 == 2606275}")


if __name__ == "__main__":
    main()

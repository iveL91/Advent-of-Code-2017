"""
    aoc_23
    https://adventofcode.com/2017/day/23
"""

from libs.aoc_23_lib import data_input, part_1, part_2


def main() -> None:
    instruction_list = data_input("data/aoc_23_data.txt")
    # letters: str = "abcdefgh"

    # Part 1
    p_1 = part_1(instruction_list)
    print(f"Part 1: {p_1} is {p_1 == 3969}")

    # Part 2
    p_2 = part_2(instruction_list)
    print(f"Part 2: {p_2} is {p_2 == 917}")


if __name__ == "__main__":
    main()

"""
    aoc_25
    https://adventofcode.com/2017/day/25
"""

from libs.aoc_25_lib import data_input, part_1


def main() -> None:
    begin_state, steps, dct = data_input("data/aoc_25_data.txt")
    tape_length: int = 10_000_000 - 1

    # Part 1
    p_1 = part_1(begin_state, steps, dct, tape_length)
    print(f"Part 1: {p_1} is {p_1 == 2725}")


if __name__ == "__main__":
    main()

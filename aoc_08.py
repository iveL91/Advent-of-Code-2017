"""
    aoc_08
    https://adventofcode.com/2017/day/8
"""

from libs.aoc_08_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_08_data.txt")

    # Part 1
    p_1 = part_1(data)
    print(f"Part 1: {p_1} is {p_1 == 5752}")

    # Part 2
    p_2 = part_2(data)
    print(f"Part 2: {p_2} is {p_2 == 6366}")


if __name__ == "__main__":
    main()

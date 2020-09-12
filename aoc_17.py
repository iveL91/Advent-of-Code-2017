"""
    aoc_17
    https://adventofcode.com/2017/day/17
"""

from libs.aoc_17_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_17_data.txt")

    # Part 1
    PART_1 = part_1(data)
    print(f"Part 1: {PART_1} is {PART_1 == 355}")

    # Part 2
    PART_2 = part_2(data)
    print(f"Part 2: {PART_2} is {PART_2 == 6154117}")


if __name__ == "__main__":
    main()

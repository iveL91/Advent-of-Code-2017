"""
    aoc_05
    https://adventofcode.com/2017/day/5
"""

from libs.aoc_05_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_05_data.txt")

    # Part 1
    p_1 = part_1(data)
    print(f"Part 1: {p_1} is {p_1 == 360603}")

    # Part 2
    p_2 = part_2(data)
    print(f"Part 2: {p_2} is {p_2 == 25347697}")


if __name__ == "__main__":
    main()

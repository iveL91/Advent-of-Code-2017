"""
    aoc_10
    https://adventofcode.com/2017/day/10
"""

from libs.aoc_10_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_10_data.txt")
    list_length: int = 256

    # Part 1
    p_1 = part_1(data, list_length)
    print(f"Part 1: {p_1} is {p_1 == 11413}")

    # Part 2
    p_2 = part_2(data, list_length)
    print(f"Part 2: {p_2} is {p_2 == '7adfd64c2a03a4968cf708d1b7fd418d'}")


if __name__ == "__main__":
    main()

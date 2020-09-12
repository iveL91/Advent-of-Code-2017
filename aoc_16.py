"""
    aoc_16
    https://adventofcode.com/2017/day/16
"""

from libs.aoc_16_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_16_data.txt")
    start_string: str = "abcdefghijklmnop"

    # Part 1
    p_1 = part_1(data, start_string)
    print(f"Part 1: {p_1} is {p_1 == 'doeaimlbnpjchfkg'}")

    # Part 2
    p_2 = part_2(data, start_string)
    print(f"Part 2: {p_2} is {p_2 == 'agndefjhibklmocp'}")


if __name__ == "__main__":
    main()

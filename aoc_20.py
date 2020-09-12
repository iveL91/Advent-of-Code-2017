"""
    aoc_20
    https://adventofcode.com/2017/day/20
"""

from libs.aoc_20_lib import data_input, part_1, part_2


def main() -> None:
    particles = data_input("data/aoc_20_data.txt")

    # Part 1
    p_1 = part_1(particles)
    print(f"Part 1: {p_1} is {p_1 == 157}")

    # Part 2
    p_2 = part_2(particles)
    print(f"Part 2: {p_2} is {p_2 == 499}")


if __name__ == "__main__":
    main()

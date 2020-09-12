"""aoc_05_lib"""

from typing import List


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read().splitlines()]


def func(data: List[int], part: int) -> int:
    position: int = 0
    counter: int = 0
    new_data: List[int] = data.copy()
    while position < len(new_data):
        add: int = 1 if (new_data[position] < 3 or part == 1) else -1
        new_data[position] += add
        position += new_data[position] - add
        counter += 1
    return counter


def part_1(data: List[int]) -> int:
    """"""
    return func(data, 1)


def part_2(data: List[int]) -> int:
    """"""
    return func(data, 2)

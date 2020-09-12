"""aoc_02_lib"""

import itertools
from typing import List


def data_input(filename: str) -> List[List[int]]:
    """"""
    with open(filename) as f:
        return [[int(element) for element in row.split("\t")] for row in f.read().splitlines()]


def part_1(data: List[List[int]]) -> int:
    """"""
    return sum(max(row) - min(row) for row in data)


def part_2(data: List[List[int]]) -> int:
    """"""
    return sum(sum(row_i // row_j
                    for (i, row_i), (j, row_j) in itertools.product(enumerate(row), enumerate(row))
                    if (row_i % row_j == 0) and (i != j))
                for row in data)

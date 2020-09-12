"""aoc_04_lib"""

from typing import List


def data_input(filename: str) -> List[List[str]]:
    """"""
    with open(filename) as f:
        return [row.split(" ") for row in f.read().splitlines()]


def func(row: list) -> bool:
    for i, row_i in enumerate(row):
        for j, row_j in enumerate(row[i+1:], i+1):
            if (row_i == row_j) and (i != j):
                return False
    return True


def part_1(data: List[List[str]]) -> int:
    """"""
    return sum(func(row) for row in data)


def func2(row: List[str]) -> bool:
    for i, word_1 in enumerate(row):
        for word_2 in row[i+1:]:
            if len(word_1) == len(word_2):
                for letter in word_1:
                    if letter in word_2:
                        word_2 = word_2.replace(letter, "", 1)
                if word_2 == "":
                    return False
    return True


def part_2(data: List[List[str]]) -> int:
    """"""
    return sum(func2(row) for row in data)

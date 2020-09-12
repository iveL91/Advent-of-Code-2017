"""aoc_19_lib"""

import itertools
from operator import add
from typing import List, Tuple


class Network:
    """"""

    def __init__(self, field: List[str], position: List[int], direction: List[int], letters_passed: str) -> None:
        """"""
        self.field = field
        self.position = position
        self.direction = direction
        self.letters_passed = letters_passed

    @property
    def field_value(self) -> str:
        return self.field[self.position[0]][self.position[1]]

    @staticmethod
    def list_add(list_1: list, list_2: list) -> list:
        return [element_1 + element_2 for element_1, element_2 in zip(list_1, list_2)]

    def direction_change(self) -> None:
        """"""
        if self.direction[0] != 0:  # Up or down
            if self.position[1] != 0:
                try:
                    left_neighbor = self.field[self.position[0]][self.position[1] - 1]
                except IndexError:
                    left_neighbor = " "
                if left_neighbor != " ":
                    self.direction = [0, -1]
                else:
                    self.direction = [0, 1]
            else:
                self.direction = [0, 1]
        else:  # Left or right
            if self.position[0] != 0:
                try:
                    upper_neighbor = self.field[self.position[0] - 1][self.position[1]]
                except IndexError:
                    upper_neighbor = " "
                if upper_neighbor != " ":
                    self.direction = [-1, 0]
                else:
                    self.direction = [1, 0]
            else:
                self.direction = [1, 0]

    def move(self) -> None:
        """"""
        self.position = self.list_add(self.position, self.direction)
        element = self.field[self.position[0]][self.position[1]]
        if element == "+":
            self.direction_change()
        elif element not in ["|", "-", "+"]:
            self.letters_passed += element


def constructor(field: List[str]) -> Tuple[str, int]:
    """"""
    position: List[int] = [0, 0]
    for index, element in enumerate(field[0]):
        if element != "":
            position[1] = index

    direction: List[int] = [1, 0]  # Down, Right

    network: Network = Network(field, position, direction, "")
    counter: int = 0
    while network.field_value != " ":
        network.move()
        counter += 1

    return network.letters_passed[:-1], counter


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split("\n")


def part_1(field: List[str]) -> str:
    """"""
    return constructor(field)[0]


def part_2(field: List[str]) -> int:
    """"""
    return constructor(field)[1]

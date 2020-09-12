"""aoc_22_lib"""

import math
from typing import List, Tuple


class GridComputingCluster:
    """"""

    def __init__(self, field: List[List[float]], position: List[int], orient: List[int], inf_counter: int, step_length: float):
        """"""
        self.field: List[List[float]] = field
        self.position: List[int] = position
        self.orient: List[int] = orient
        self.inf_counter: int = inf_counter
        self.step_length: float = step_length

    @property
    def field_value(self) -> float:
        return self.field[self.position[0]][self.position[1]]

    @field_value.setter
    def field_value(self, value: float) -> float:
        self.field[self.position[0]][self.position[1]] = value

    def orientation(self):
        """"""
        new_orient = {
            1: [self.orient[1], -self.orient[0]],
            0: [-self.orient[1], self.orient[0]], 
            0.5: self.orient,
            1.5: [-self.orient[0], -self.orient[1]]
        }
        self.orient = new_orient[self.field_value]

    def infecting(self):
        """"""
        self.field_value += self.step_length
        self.field_value %= 2
        if self.field_value == 1:
            self.inf_counter += 1

    def moving(self):
        """"""
        self.position = [sum(x) for x in zip(self.position, self.orient)]

    def burst(self):
        """"""
        self.orientation()
        self.infecting()
        self.moving()


def data_input(filename: str) -> Tuple[List[List[float]], List[int]]:
    """"""
    with open(filename) as f:
        data = f.read().replace("#", "1").replace(".", "0").split("\n")

        field_size: int = 10000 - 1
        start_field: List[List[float]] = [[0 for _ in range(field_size)] for _ in range(field_size)]

        for i, dataline in enumerate(data):
            for j, datapoint in enumerate(dataline):
                x = i + math.ceil(field_size / 2) - math.ceil(len(data) / 2)
                y = j + math.ceil(field_size / 2) - math.ceil(len(data) / 2)
                start_field[x][y] = int(datapoint)

        start_position = [math.ceil(field_size / 2) - 1, math.ceil(field_size / 2) - 1]
        return start_field, start_position


def constructor(start_field: List[List[float]], start_position: List[int], start_orient: List[int], bursts: int, step_length: float):
    """"""
    grid_computing_cluster = GridComputingCluster(start_field, start_position, start_orient, inf_counter=0, step_length=step_length)

    for _ in range(bursts):
        grid_computing_cluster.burst()

    return grid_computing_cluster.inf_counter


def part_1(start_field: List[List[float]], start_position: List[int], start_orient: List[int]) -> int:
    """"""
    return constructor(start_field, start_position, start_orient, 10_000, 1)


def part_2(start_field: List[List[float]], start_position: List[int], start_orient: List[int]) -> int:
    """"""
    return constructor(start_field, start_position, start_orient, 10_000_000, 0.5)

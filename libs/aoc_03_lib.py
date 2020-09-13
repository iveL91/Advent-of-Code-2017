"""aoc_03_lib"""

import copy
import itertools
from math import sqrt
from typing import Callable, Dict, List
from libs.timer import timer


def data_input(filename: str) -> int:
    """"""
    with open(filename) as f:
        return int(f.read())


def layer(point: int) -> int:
    if not int(sqrt(point)) % 2:
        return int(sqrt(point)) // 2
    elif sqrt(point) % 1:
        return (int(sqrt(point)) + 1) // 2
    else:
        return (int(sqrt(point)) - 1) // 2


def way_length(point: int) -> int:
    layer_point: int = layer(point)
    return layer_point + abs(((point - (2*layer_point-1)**2) % (2*layer_point)) - layer_point) if layer_point else 0


@timer
def part_1(data: int) -> int:
    return way_length(data)


class Grid2D:
    def __init__(self, grid_size: int) -> None:
        self.grid_size = grid_size
        self.diameter: int = grid_size // 2
        self.center: int = grid_size // 2
        self.grid: List[List[int]] = [
            [0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid[self.center][self.center] = 1
        self.outside: bool = False
        self.first_outside: int = 0

    def sum_adjecent(self, x: int, y: int) -> int:
        return -self.grid[x][y] + sum(self.grid[x-1+i][y+1-j] for i, j in itertools.product(range(3), range(3)))

    def is_outside(self, data: int, sum_adj: int) -> None:
        if sum_adj > data and not self.outside:
            self.outside = True
            self.first_outside = copy.copy(sum_adj)

    def step(self, data: int, x, y) -> None:
        sum_adj = self.sum_adjecent(x, y)
        self.grid[x][y] = sum_adj
        self.is_outside(data, sum_adj)

    def side(self, data, lyr, direction):
        if not self.outside:
            for i in range(2 * lyr):
                if self.outside:
                    break
                else:
                    self.step(data, *direction(i))


@timer
def part_2(data: int) -> int:
    """"""
    grid2d = Grid2D(13)
    layer_directions: Callable = lambda lyr: {"east": lambda i: (grid2d.center + lyr, grid2d.center - lyr + 1 + i),
                                              "north": lambda i: (grid2d.center + lyr - i - 1, grid2d.center + lyr),
                                              "west": lambda i: (grid2d.center - lyr, grid2d.center + lyr - 1 - i),
                                              "south": lambda i: (grid2d.center - lyr + 1 + i, grid2d.center - lyr)}

    for lyr in range(1, grid2d.diameter - 1):
        for direction in layer_directions(lyr).values():
            grid2d.side(data, lyr, direction)
    return grid2d.first_outside

"""aoc_07_lib"""

import itertools
import re
from typing import Any, List, Match, Optional
from libs.timer import timer


class Tower:
    """Tower class"""
    dataset: List[str] = []

    def __init__(self, tower_str: str) -> None:
        """"""
        split: List[str] = tower_str.split(" -> ")
        x: Optional[Match] = re.search(r"(\w+) [(](\d+)[)]", split[0])
        self.name: str = str(x.group(1))
        self.weight: int = int(x.group(2))
        self.subtowers_list = split[1].split(", ") if len(split) > 1 else []

    def subtowers(self) -> List[Any]:
        """"""
        subtowers_long: List[Tower] = []
        for subtower, string in itertools.product(self.subtowers_list, self.dataset):
            x: Optional[Match] = re.search(subtower + r" [(](\d+)[)]", string)
            if x is not None:
                subtowers_long.append(Tower(string))
        return subtowers_long

    def unbalanced_tower(self) -> Optional[Any]:
        """"""
        unbalanced_tower: Optional[Tower] = None
        if self.subtowers():
            subtower1 = self.subtowers()[0]
            for subtower2 in self.subtowers():
                if subtower1.total_weight() != subtower2.total_weight():
                    for subtower3 in self.subtowers():
                        if (subtower1 != subtower3) and \
                                (subtower1.total_weight() != subtower3.total_weight()):
                            unbalanced_tower = subtower1
                        else:
                            unbalanced_tower = subtower2
                    break
        return unbalanced_tower

    def balance(self) -> bool:
        """"""
        return not self.unbalanced_tower()

    def subtowers_weight(self) -> int:
        """"""
        return sum(subtower.total_weight() for subtower in self.subtowers())

    def total_weight(self) -> int:
        """"""
        return self.weight+self.subtowers_weight()


def bottom_tower(dataset: List[str]) -> Tower:
    """"""
    bottom_tow: Optional[Tower] = None
    for tower1 in dataset:
        found: bool = True
        for tower2 in dataset:
            if Tower(tower1).name in Tower(tower2).subtowers_list:
                found = False
                break
        if found:
            bottom_tow = tower1
    return Tower(bottom_tow)


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split("\n")


@timer
def part_1(data: List[str]) -> str:
    """"""
    Tower.dataset = data
    return bottom_tower(data).name


@timer
def part_2(data: List[str]) -> int:
    """"""
    Tower.dataset = data
    tower: Tower = bottom_tower(data)
    bal: bool = tower.balance()
    while not bal:
        bal = True
        for subtower in tower.unbalanced_tower().subtowers():
            if subtower.unbalanced_tower() is not None:
                tower = subtower
                bal = False
                break

    total_weight_list = [subtower.total_weight()
                         for subtower in tower.subtowers()]

    return tower.unbalanced_tower().weight - (max(total_weight_list) - min(total_weight_list))

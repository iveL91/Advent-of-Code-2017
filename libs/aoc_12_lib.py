"""aoc_12_lib"""

import re
from typing import Dict, List, Pattern, Set, Tuple


def data_input(filename: str) -> str:
    """"""
    with open(filename) as f:
        return f.read()


def id_circle(connections_dict: Dict[int, List[int]], ends: List[int], containing_id: Set[int]) -> Set[int]:
    """"""
    new_containing_id: Set[int] = containing_id.union(ends)
    if new_containing_id.difference(containing_id):
        for end in ends:
            new_containing_id = id_circle(
                connections_dict, connections_dict[end], new_containing_id)

    return new_containing_id


def construction(data: str) -> Dict[int, Set[int]]:
    """"""
    connections_dict: Dict[int, List[int]] = {}
    pattern: Pattern = re.compile(r"(\d+) <-> (.+)")
    matches: List[Tuple[str, str]] = re.findall(pattern, data)
    for match in matches:
        connections_dict[int(match[0])] = [int(element) for element in match[1].split(
            ", ")] if len(match[1]) > 1 else [int(match[1])]

    containing_id_dict: Dict[int, Set[int]] = {}
    lst: List[int] = []
    for key, value in connections_dict.items():
        if key not in lst:
            containing_id_dict[key] = id_circle(connections_dict, value, {key})
            lst += containing_id_dict[key]

    return containing_id_dict


def part_1(data: str) -> int:
    """"""
    return len(construction(data)[0])


def part_2(data: str) -> int:
    """"""
    return len(construction(data))

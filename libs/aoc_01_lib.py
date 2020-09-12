"""aoc_01_lib"""


def data_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def part_1(data: str) -> int:
    data_extend: str = data + data[0]
    return sum(int(data_extend[i]) for i, _ in enumerate(data) if data_extend[i] == data_extend[i+1])


def part_2(data: str) -> int:
    data_twice: str = data + data
    half_length: int = len(data) // 2
    return sum(int(data_twice[i]) for i, _ in enumerate(data) if data_twice[i] == data_twice[i+half_length])

"""hash"""

from typing import List, Tuple


def knotting(lengths: List[int], lst: List[int], current_position: int, skip_size: int, list_length: int = 256) -> Tuple[List[int], int, int]:
    """"""
    for length in lengths:
        string: List[int] = [lst[(current_position+i) % list_length]
                             for i in range(length)]
        string = string[::-1]
        for i, str_i in enumerate(string):
            lst[(current_position+i) % list_length] = str_i
        current_position += length + skip_size
        skip_size += 1
    return lst, current_position, skip_size


def xor_list(numbers: List[int]) -> int:
    """"""
    number: int = 0
    for element in numbers:
        number ^= element
    return number


def dense_hash(sparse_hash: List[int]) -> List[int]:
    return [xor_list([sparse_hash[16 * i + j] for j in range(16)]) for i in range(16)]


def knot_hash(dataset: str, list_length: int = 256) -> str:
    """"""
    lengths_ascii = [ord(data) for data in dataset]
    lengths_suffix: List[int] = [17, 31, 73, 47, 23]
    lengths = lengths_ascii + lengths_suffix
    rounds: int = 64
    lst = [n for n in range(list_length)]
    current_position: int = 0
    skip_size: int = 0
    sparse_hash: List[int] = []

    for _ in range(rounds):
        sparse_hash, current_position, skip_size = knotting(
            lengths, lst, current_position, skip_size, list_length)

    dense_hash_list = dense_hash(sparse_hash)
    hex_string_list = ["%0.2X" %
                       number for number in dense_hash_list]
    hex_string = "".join(hex_string_list)

    return hex_string

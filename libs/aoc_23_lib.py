"""aoc_23_lib"""

import libs.program as program
from typing import List


class ExperimentalCoprocessor(program.Program):
    """"""

    def __init__(self, instruction_lst: List[List[str]]) -> None:
        """"""
        super().__init__(instruction_lst)

    def move(self) -> None:
        self.command_dict[self.code]()

    def start(self) -> None:
        """Initial set-up[1:8] (list, integer, dict -> integer, dict)"""
        while self.position < 8:
            self.move()

    def loop(self) -> None:
        """Loop[9:32] (integer, dict -> integer, dict)"""
        self.dct["f"] = 1
        # dct["e"] = dct["b"]
        # dct["d"] = dct["b"]
        if not is_prime(self.dct["b"]):
            self.dct["f"] = 0
        if not self.dct["f"]:
            self.dct["h"] -= -1
        self.dct["g"] = self.dct["b"] - self.dct["c"]
        self.position += 19
        if not self.dct["g"]:
            self.position += 4
        else:
            self.dct["b"] -= -17
            self.position -= 19

    def run(self) -> None:
        # Initializing
        self.start()
        # Getting into the loop for the first time
        self.move()
        self.move()
        self.move()

        while self.position < len(self.instruction_lst):
            self.loop()


def is_prime(n: int) -> bool:
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def data_input(filename: str) -> List[List[str]]:
    """"""
    with open(filename) as f:
        return [row.split(" ") for row in f.read().split("\n")]


def part_1(instruction_lst: List[List[str]]) -> int:
    """"""
    experimental_coprocessor = ExperimentalCoprocessor(
        instruction_lst)
    mul_counter: int = 0

    while experimental_coprocessor.position < len(instruction_lst):
        if experimental_coprocessor.code == "mul":
            mul_counter += 1
        experimental_coprocessor.move()

    return mul_counter


def part_2(instruction_lst: List[List[str]]) -> int:
    """"""
    experimental_coprocessor = ExperimentalCoprocessor(
        instruction_lst)
    experimental_coprocessor.dct["a"] = 1
    experimental_coprocessor.run()

    return experimental_coprocessor.dct["h"]

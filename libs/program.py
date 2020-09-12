"""program"""

import operator
import re
from typing import Callable, Dict, List, Optional, Set


def value(string: str, dct: Dict[str, int]) -> int:
    """"""
    try:
        return int(string)
    except ValueError:
        return dct[string]


class Program:
    def __init__(self, instruction_lst: List[List[str]]) -> None:
        self.instruction_lst = instruction_lst
        letters: Set[str] = {instruction[1] for instruction in self.instruction_lst if
                             re.search(r"\D", instruction[1])}
        self.dct: Dict[str, int] = {letter: 0 for letter in letters}
        self.position: int = 0
        self.queue: List[Optional[int]] = []
        self.counter: int = 0
        self.command_dict: Dict[str, Callable] = {
            "add": addCommand(self),
            "sub": subCommand(self),
            "mul": mulCommand(self),
            "mod": modCommand(self),
            "set": setCommand(self),
            "jgz": jgzCommand(self),
            "jnz": jnzCommand(self)
        }

    @property
    def code(self) -> str:
        return self.instruction_lst[self.position][0]


class ProgramCommand:
    def __init__(self, program: Program) -> None:
        self.program = program


class setCommand(ProgramCommand):
    def __call__(self) -> None:
        self.program.dct[self.program.instruction_lst[self.program.position][1]] = value(
            self.program.instruction_lst[self.program.position][2], self.program.dct)
        self.program.position += 1


class BinaryCommand(ProgramCommand):
    def __init__(self, program: Program, operator: Callable) -> None:
        super().__init__(program)
        self.operator = operator

    def __call__(self) -> None:
        self.program.dct[self.program.instruction_lst[self.program.position][1]] = self.operator(
            self.program.dct[self.program.instruction_lst[self.program.position][1]], value(self.program.instruction_lst[self.program.position][2], self.program.dct))
        self.program.position += 1


class addCommand(BinaryCommand):
    def __init__(self, program: Program) -> None:
        super().__init__(program, operator.add)


class subCommand(BinaryCommand):
    def __init__(self, program: Program) -> None:
        super().__init__(program, operator.sub)


class mulCommand(BinaryCommand):
    def __init__(self, program: Program) -> None:
        super().__init__(program, operator.mul)


class modCommand(BinaryCommand):
    def __init__(self, program: Program) -> None:
        super().__init__(program, operator.mod)


class jumpCommand(ProgramCommand):
    def __init__(self, program: Program, operator: Callable) -> None:
        super().__init__(program)
        self.operator = operator

    def __call__(self) -> None:
        if self.operator(value(self.program.instruction_lst[self.program.position][1], self.program.dct), 0):
            self.program.position += value(
                self.program.instruction_lst[self.program.position][2], self.program.dct)
        else:
            self.program.position += 1


class jgzCommand(jumpCommand):
    def __init__(self, program: Program) -> None:
        super().__init__(program, operator.gt)


class jnzCommand(jumpCommand):
    def __init__(self, program: Program) -> None:
        super().__init__(program, operator.ne)

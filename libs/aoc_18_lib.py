"""aoc_18_lib"""

from typing import Dict, List
import libs.program as program


def data_input(filename: str) -> List[List[str]]:
    """"""
    with open(filename) as f:
        return [row.split(" ") for row in f.read().split("\n")]


class Duet:
    def __init__(self, instruction_lst) -> None:
        self.instruction_lst = instruction_lst
        self.programs = (program.Program(self.instruction_lst),
                         program.Program(self.instruction_lst))
        self.programs[1].dct["p"] = 1
        self.index: int = 0

    @property
    def program(self) -> program.Program:
        return self.programs[self.index]

    def move(self) -> None:
        command_dict = {
            "add": program.addCommand(self.program),
            "mul": program.mulCommand(self.program),
            "mod": program.modCommand(self.program),
            "set": program.setCommand(self.program),
            "jgz": program.jgzCommand(self.program),
            "snd": sndCommand(self),
            "rcv": rcvCommand(self)
        }
        command_dict[self.program.code]()

    def run1(self) -> None:
        while not self.index and (0 <= self.program.position < len(self.instruction_lst)):
            self.move()

    def run2(self) -> None:
        while (self.programs[0].queue != [] or self.programs[1].queue != []
               or (not self.programs[0].counter or not self.programs[1].counter))\
                and (0 <= self.program.position < len(self.instruction_lst)):
            self.move()


class DuetCommand:
    def __init__(self, duet: Duet) -> None:
        self.duet = duet


class sndCommand(DuetCommand):
    def __call__(self) -> None:
        self.duet.programs[self.duet.index ^ 1].queue.append(program.value(
            self.duet.program.instruction_lst[self.duet.program.position][1], self.duet.program.dct))
        self.duet.program.counter += 1
        self.duet.program.position += 1


class rcvCommand(DuetCommand):
    def __call__(self) -> None:
        if self.duet.program.queue:
            self.duet.program.dct[self.duet.instruction_lst[self.duet.program.position]
                                  [1]] = self.duet.program.queue.pop(0)
            self.duet.program.position += 1
        else:
            self.duet.index ^= 1


def part_1(instruction_lst: List[List[str]]) -> int:
    """"""
    duet = Duet(instruction_lst)
    duet.run1()
    return duet.program.queue[-1]


def part_2(instruction_lst: List[List[str]]) -> int:
    """"""
    duet = Duet(instruction_lst)
    duet.run1()
    duet.run2()
    return duet.programs[1].counter

"""aoc_21_lib"""

import functools
import itertools
import re
import numpy as np
from typing import List
from libs.timer import timer


def create_matrix(string: str, reg_ex_raw: str):
    """"""
    pattern = re.compile(reg_ex_raw)
    match = re.search(pattern, string)
    dim_input = len(match.group(1))
    matrix = np.zeros((dim_input, dim_input), dtype=np.dtype(np.int16))
    for i, j in itertools.product(range(dim_input), range(dim_input)):
        matrix[i, j] = int(match.group(i + 1).zfill(dim_input)[j])
    return matrix


def data_input(filename: str) -> list:
    """"""
    with open(filename) as f:
        file = f.read().replace("#", "1").replace(".", "0").split("\n")
        input_reg_ex: str = r"(\d+)\/(\d+)\/?(\d*)? "
        output_reg_ex: str = r" (\d+)\/(\d+)\/(\d+)\/?(\d*)?"
        return [(create_matrix(dataline, input_reg_ex), create_matrix(dataline, output_reg_ex)) for dataline in file]


def complete_instruction_dict(instruction_list: list) -> dict:
    flips = [identity, flip_horizontal, flip_vertical]
    rotations = [identity, rotate_90, rotate_180, rotate_270]
    result = {}
    for inpt, output in instruction_list:
        for flip, rotation in itertools.product(flips, rotations):
            result[tuple(map(tuple, flip(rotation(inpt))))] = output
    return result


def repeated(f, n):
    """From https://stackoverflow.com/questions/22921626/how-to-compose-to-functions-several-times"""
    def repeat(arg):
        return functools.reduce(lambda r, g: g(r), [f] * n, arg)
    return repeat


def identity(matrix):
    """(np.array -> np.array)"""
    return matrix


def rotate_90(matrix):
    """(np.array -> np.array)"""
    dim_x, dim_y = matrix.shape
    new_matrix = np.zeros((dim_y, dim_x), dtype=np.dtype(np.int16))
    for i in range(int(min(dim_x, dim_y)/2)+1):
        for y, x in itertools.product(range(i, dim_x-i), range(i, dim_y-i)):
            if y == i:
                new_matrix[x, y] = matrix[i, (dim_y-1)-x]
            elif x == dim_y-1-i:
                new_matrix[x, y] = matrix[y, i]
            elif y == dim_x-1-i:
                new_matrix[x, y] = matrix[dim_x-1-i, (dim_y-1)-x]
            elif x == i:
                new_matrix[x, y] = matrix[y, dim_y-1-i]
    return new_matrix


def rotate_180(matrix):
    """(np.array -> np.array)"""
    return repeated(rotate_90, 2)(matrix)


def rotate_270(matrix):
    """(np.array -> np.array)"""
    return repeated(rotate_90, 3)(matrix)


def flip_horizontal(matrix):
    """(np.array -> np.array)"""
    dim, _ = matrix.shape
    flip_matrix = rotate_90(np.eye(dim, dtype=np.dtype(np.int16)))
    return flip_matrix @ matrix


def flip_vertical(matrix):
    """(np.array -> np.array)"""
    _, dim = matrix.shape
    flip_matrix = rotate_90(np.eye(dim))
    return matrix @ flip_matrix


def slicing(matrix, width: int, height: int) -> list:
    """(np.array, integer, integer -> list)"""
    dim_x, dim_y = matrix.shape
    nr_slices_x: int = dim_x // height
    nr_slices_y: int = dim_y // width
    return ((matrix[i*height:(i+1)*height, j*width:(j+1)*width] for j in range(nr_slices_y)) for i in range(nr_slices_x))


def gluing_horizontal2(matrix1, matrix2):
    """(np.array, np.array -> np.array)"""
    dim_x_1, dim_y_1 = matrix1.shape
    dim_x_2, dim_y_2 = matrix2.shape
    dim_y: int = dim_y_1 + dim_y_2
    if dim_x_1 == dim_x_2:
        dim_x: int = dim_x_1
        return np.array([[matrix1[x, y] if y < dim_y_1 else matrix2[x, y-dim_y_1] for y in range(dim_y)] for x in range(dim_x)])
    else:
        return "Different heights!"


@timer
def gluing_horizontal(matrices):
    """(list -> np.array)"""
    return functools.reduce(gluing_horizontal2, matrices)



def gluing_vertical2(matrix1, matrix2):
    """(np.array, np.array -> np.array)"""
    dim_x_1, dim_y_1 = matrix1.shape
    dim_x_2, dim_y_2 = matrix2.shape
    dim_x: int = dim_x_1 + dim_x_2
    if dim_y_1 == dim_y_2:
        dim_y: int = dim_y_1
        return np.array([[matrix1[x, y] if x < dim_x_1 else matrix2[x-dim_x_1, y] for y in range(dim_y)] for x in range(dim_x)])
    else:
        return "Different widths!"


def gluing_vertical(matrices):
    """(list -> np.array)"""
    return functools.reduce(gluing_vertical2, matrices)


def gluing(list_list_matrices: list):
    """(list -> np.array)"""
    return gluing_vertical(gluing_horizontal(list_matrices) for list_matrices in list_list_matrices)

@timer
def iteration(ins_in_out: list, matrix):
    """(list, list, list, np.array -> np.array)"""
    size, _ = matrix.shape
    slices: list
    if not size % 2:
        slices = slicing(matrix, 2, 2)
    elif not size % 3:
        slices = slicing(matrix, 3, 3)
    trans_slices = ((ins_in_out[tuple(map(tuple, mat))]
                     for mat in mat_slice) for mat_slice in slices)
    return gluing(trans_slices)


def constructor(instructions_in_out: list, rounds: int) -> int:
    """"""
    matrix = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]],
                      dtype=np.dtype(np.int16))
    # counter = 0
    # print(counter)
    for _ in range(rounds):
        matrix = iteration(instructions_in_out, matrix)
        # counter += 1
        # print(counter)

    return np.count_nonzero(matrix == 1)


@timer
def part_1(instructions_in_out: list, rounds: int = 5) -> int:
    """"""
    return constructor(complete_instruction_dict(instructions_in_out), rounds)


@timer
def part_2(instructions_in_out: list) -> int:
    """"""
    rounds: int = 18
    return constructor(complete_instruction_dict(instructions_in_out), rounds)

from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[100:150, 100:150] = 1
    #res[300: ,200:] = 1
    # this is my proposal for the left half mask:
    res[240:340, :320] = 1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    # res[100:150, 100:300] = -1
    # this is my proposal for the right half mask:
    res[240:340,321: ] = 1
    return res

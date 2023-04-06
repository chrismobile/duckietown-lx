from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[100:150, 100:150] = 1
    #res[300:, 200:] = 1
    # this is my proposal
    res[240: , :320] = 1    # close encounter on left side -> accelerates left wheel
    #res[240: , 321: ] = -1   # close encounter on right side -> decelerates left wheel
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    # res[100:150, 100:300] = -1
    # this is my proposal
    res[240: , 321: ] = 1   # close encounter on right side -> accelerates right wheel
    #res[240: , :320] = -1  # close encounter on left side -> decelerates right wheel
    return res

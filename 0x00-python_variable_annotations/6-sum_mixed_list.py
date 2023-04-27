#!/usr/bin/env python3
"""A type-annotated function that returns the sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function that returns the sum of mixed ints and floats in a list"""
    return sum(mxd_list)

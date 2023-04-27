#!/usr/bin/env python3
"""A type-annotated function that returns the sum as a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function that returns the sum of floats in a list"""
    return sum(input_list)

#!/usr/bin/env python3
"""Define a type-annotated function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """Function that returns a """
    def mult(x: float) -> float:
        return x * multiplier
    return mult

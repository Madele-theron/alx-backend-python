#!/usr/bin/env python3
"""Define a type-annotated function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a function that multiplies a float by the multiplier"""
    def mult(x: float) -> float:
        return x * multiplier
    return mult

#!/usr/bin/env python3
"""Define a type-annotated function that returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """Function that returns a tuple, 1-string, 2-float"""
    return (k, v * v)

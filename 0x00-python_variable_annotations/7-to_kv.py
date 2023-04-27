#!/usr/bin/env python3
"""Define a type-annotated function that returns a tuple"""
from typing import Union


def to_kv(k: str, v: Union[float, int]) -> tuple[str, float]:
    """Function that returns a tuple, 1st el =  """
    return (k, v ** 2)

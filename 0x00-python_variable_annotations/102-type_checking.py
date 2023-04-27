#!/usr/bin/env python3
"""Type Checking - Validate code and fix errors """
from typing import Tuple, List
from math import floor


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return values with the appropriate types """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, floor(3.0))

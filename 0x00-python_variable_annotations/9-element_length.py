#!/usr/bin/env python3
"""Define a type-annotated function to learn Duck Typing"""
from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Annotate the below functions parameters return appropriate types"""
    return [(i, len(i)) for i in lst]

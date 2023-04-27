#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Union, Any, TypeVar, Mapping

# define a type variable T
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, 
                    default: Union[T, None] = None) -> Union[Any, T]:
    """Augmented code with correct duck typed annotations"""
    if key in dct:
        return dct[key]
    else:
        return default

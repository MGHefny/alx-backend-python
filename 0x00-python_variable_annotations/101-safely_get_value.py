#!/usr/bin/env python3
"""Task 101 dev"""
from typing import Any, Mapping, Union, TypeVar


x = TypeVar("x")
y = Union[Any, x]
z = Union[x, None]


def safely_get_value(dct: Mapping, key: Any, default: z = None) -> y:
    """value dict given key"""
    if key in dct:
        return dct[key]
    else:
        return default

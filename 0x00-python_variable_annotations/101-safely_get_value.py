#!/usr/bin/env python3
"""Task 101 dev"""
from typing import Any, Mapping, Union, TypeVar


x = TypeVar("x")
k = Union[Any, x]
v = Union[x, None]


def safely_get_value(dct: Mapping, key: Any, default: v = None) -> k:
    """value dict given key"""
    if key in dct:
        return dct[key]
    else:
        return default

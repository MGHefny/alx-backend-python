#!/usr/bin/env python3
"""Task 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier function"""
    return lambda n: n * multiplier

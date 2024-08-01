#!/usr/bin/env python3
"""Task 9"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """length list seq"""
    return [(x, len(x)) for x in lst]

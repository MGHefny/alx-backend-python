#!/usr/bin/env python3
"""Task 100 adv"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """first element seq exists"""
    if lst:
        return lst[0]
    else:
        return None

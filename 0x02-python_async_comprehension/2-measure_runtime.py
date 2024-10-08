#!/usr/bin/env python3
"""Task 2"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ "4 times and execution time"""
    start = time.time()
    order = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*order)
    return time.time() - start

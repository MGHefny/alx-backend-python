#!/usr/bin/env python3
"""Tsak 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """make function wait time"""
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time

#!/usr/bin/env python3
"""A module that measures run time for four parallel comprehensions."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_generator four times in parallel using asyncio.gather.

    Args:
        None

    Return:
        The total runtime as a float number
    """
    start_time = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()

    return (end_time - start_time)

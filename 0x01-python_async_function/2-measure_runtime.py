#!/usr/bin/env python3
"""A module that Measure the runtime of an aync function
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Measures the average execution time of wait_n(n, max_delay).

    Args:
        n: An integer = number of times to call wait_random.
        max_delay: An integer = maximum delay to use for each call.

    Returns:
        A float = average execution time of wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(max_delay, n))
    total_time = time.time() - start_time
    return total_time / n

#!/usr/bin/env python3
"""A module that executes multiple coroutines at the same time with async
"""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    An asynchronous coroutine that spawns `n` instances of the
    `task_wait_random` coroutine with the specified `max_delay`,
    and returns a list of the delay values in ascending order.

    Args:
        n (int): The number of times to spawn the `wait_random` coroutine.
        max_delay (int): The maximum delay time for each call to
            `task_wait_random`.

    Returns:
        List[float]: A list of the delay times, sorted in ascending order.
    """
    delays: List[float] = []
    semaphore = asyncio.Semaphore(n)

    async def call_task_wait_random(semaphore):
        async with semaphore:
            delay = await task_wait_random(max_delay)
            delays.append(delay)

    coroutines = [call_task_wait_random(semaphore) for _ in range(n)]
    await asyncio.gather(*coroutines)
    return sorted(delays)

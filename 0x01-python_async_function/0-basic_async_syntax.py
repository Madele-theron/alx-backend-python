#!/usr/bin/env python3
"""A module with an asynchronous coroutine that waits for a random delay"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    An asynchronous coroutine that waits for a random delay between 0 and
    `max_delay` (inclusive) seconds, and returns that delay as a floating point
    number.

    Args:
        max_delay (float, optional): The maximum amount of time (in seconds)
            that the coroutine should wait before returning. Defaults to 10.

    Returns:
        float: Random delay in seconds.

    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

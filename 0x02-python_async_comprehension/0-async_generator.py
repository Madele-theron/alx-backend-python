#!/usr/bin/env python3
"""A module with a coroutine called async_generator that takes no arguments."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields a random float between 0 and 10
    every second for 10 iterations.

    Args:
        None

    Yields:
        int: A random float between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

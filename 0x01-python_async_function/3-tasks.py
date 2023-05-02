#!/usr/bin/env python3
"""A module that creates a asyncio task
"""
import asyncio
import random
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that waits for a random delay between
    0 and max_delay seconds (float) before returning the delay time.

    Args:
        max_delay: An integer = the maximum delay time.

    Returns:
        An asyncio.Task object = the coroutine task.
    """
    async_task = asyncio.create_task(wait_random(max_delay))

    return async_task

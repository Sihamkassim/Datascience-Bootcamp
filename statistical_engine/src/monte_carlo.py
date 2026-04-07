import random

CRASH_PROBABILITY = 0.045


def simulate_crashes(days: int):
    if days <= 0:
        raise ValueError("Days must be positive.")

    crashes = 0

    for _ in range(days):
        if random.random() < CRASH_PROBABILITY:
            crashes += 1

    return crashes / days
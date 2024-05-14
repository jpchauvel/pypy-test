#!/usr/bin/env python3
import random
import argparse
import time
from typing import Callable


def calculate_pi(n: int) -> float:
    hits = 0
    for _ in range(n):
        x: float = random.uniform(.0, 1.)
        y: float = random.uniform(.0, 1.)
        if x**2 + y**2 <= 1:
            hits += 1
    return 4 * hits / n


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate π using Monte Carlo"
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=1000000,
        help="number of random points to use",
    )
    parser.add_argument(
        "-j",
        "--numba",
        action="store_true",
        help="use numba to speed up calculation",
    )
    args = parser.parse_args()
    func: Callable | None = None
    if args.numba:
        from numba_pi import calculate_pi_numba

        func = calculate_pi_numba
    else:
        func = calculate_pi

    start: float = time.time()
    pi = func(args.num)
    end: float = time.time()
    print(f"Pi = {pi}, elapsed time = {end - start} second(s)")

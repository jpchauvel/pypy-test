import random

import numpy as np
from numpy._typing import NDArray
from numba import njit, prange


@njit(parallel=True, fastmath=True)
def calculate_pi_numba(n: int) -> np.float64:
    hits: NDArray[np.float64] = np.zeros(n, dtype=np.float64)
    for i in prange(n):
        x: float = random.uniform(.0, 1.)
        y: float = random.uniform(.0, 1.)
        if x**2 + y**2 <= 1:
            hits[i] = 1.
    return 4 * np.sum(hits) / n

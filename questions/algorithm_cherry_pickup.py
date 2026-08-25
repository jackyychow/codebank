# Source: Akuna
# Question: Maximize cherries collected along two paths through a grid.
#

from typing import List
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Algorithm:
        t is total steps taken so far. Columns derive from t: c1 = t - r1, c2 = t - r2.
        """
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}

        def dp(r1: int, r2: int, t: int) -> int:
            c1 = t - r1
            c2 = t - r2
            if (r1, r2, t) in memo:
                return memo[(r1, r2, t)]
            # bounds and blocked checks
            if r1 < 0 or r2 < 0 or c1 < 0 or c2 < 0:
                return float("-inf")
            if r1 >= ROWS or r2 >= ROWS or c1 >= COLS or c2 >= COLS:
                return float("-inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")

            # goal: both robots reach bottom-right
            if r1 == ROWS - 1 and c1 == COLS - 1 and r2 == ROWS - 1 and c2 == COLS - 1:
                return grid[r1][c1]

            cherries = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]

            next_t = t + 1
            best_next = max(
                dp(r1 + 1, r2 + 1, next_t),  # both move down
                dp(r1 + 1, r2, next_t),  # r1 down, r2 right
                dp(r1, r2 + 1, next_t),  # r1 right, r2 down
                dp(r1, r2, next_t),  # both move right
            )

            if best_next == float("-inf"):
                memo[(r1, r2, t)] = float("-inf")
            else:
                memo[(r1, r2, t)] = cherries + best_next
            return memo[(r1, r2, t)]

        res = dp(0, 0, 0)
        return 0 if res == float("-inf") else res

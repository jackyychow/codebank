# Question: Find the final column for each ball dropped through a grid.
#
# LeetCode 1706: Where Will the Ball Fall.
# Q:
# 1. what is the magnitude of n we are looking at?
# 2.can i assume if a ball gets stuck in the middle of the rows in a V shape,
# or if it get stuck to a wall, i return -1 for it?
# 3. for the the last row, if it doesnt get stuck,
# do i return the column of it or the next column it rolls into?
# 4. magnitude of m, n
from typing import List


class GridSimulation:
    def __init__(self, grid: List[List[int]]):
        self.version = 1
        self.mem = {}
        self.grid = grid

    def updateGrid(self, row: int, col: int) -> None:
        #   Simpler option: remove versioning and call self.mem.clear() inside updateGrid().
        self.grid[row][col] *= -1
        self.version += 1

    def findBall(self) -> List[int]:
        #  1: \
        # -1: /
        numRow, numCol = len(self.grid), len(self.grid[0])

        def _is_blocked(row, col):
            if self.grid[row][col] == 1:
                return col == numCol - 1 or self.grid[row][col + 1] == -1

            return col == 0 or self.grid[row][col - 1] == 1

        def dropBall(row, col):
            if (self.version, row, col) in self.mem:
                return self.mem[(self.version, row, col)]
            if col < 0 or col >= numCol or _is_blocked(row, col):
                self.mem[(self.version, row, col)] = -1
            elif row == numRow - 1:
                self.mem[(self.version, row, col)] = col + self.grid[row][col]
            else:
                self.mem[(self.version, row, col)] = dropBall(
                    row + 1, col + self.grid[row][col]
                )
            return self.mem[(self.version, row, col)]

        return [dropBall(0, col) for col in range(numCol)]


if __name__ == "__main__":
    grid = [
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1],
    ]
    assert GridSimulation(grid).findBall() == [1, -1, -1, -1, -1]
    assert GridSimulation([[1]]).findBall() == [-1]

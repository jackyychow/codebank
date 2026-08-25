# Source: Akuna
# Question: Count islands in a binary grid.
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def spread(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for ix, jx in direction:
                new_i, new_j = i + ix, j + jx
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1":
                    spread(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    spread(i, j)

        return count

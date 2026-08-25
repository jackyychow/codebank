# Source: Akuna
# Question: Apply flood fill from a starting cell.
#

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        ori_color = image[sr][sc]
        m, n = len(image), len(image[0])
        visited = set()

        def dfs(i, j):
            if (i, j) in visited or image[i][j] != ori_color:
                return
            visited.add((i, j))
            image[i][j] = color
            direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for ix, jx in direction:
                new_i, new_j = i + ix, j + jx
                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and image[new_i][new_j] == ori_color
                ):
                    dfs(new_i, new_j)

        dfs(sr, sc)
        return image

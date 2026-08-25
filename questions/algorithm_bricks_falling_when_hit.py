# Source: Tower Capital
# Question: Solve Bricks Falling When Hit with multiple approaches.
#

# https://leetcode.com/problems/bricks-falling-when-hit/description/

# 803. Bricks Falling When Hit

# You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

# It is directly connected to the top of the grid, or
# At least one other brick in its four adjacent cells is stable.
# You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). 
# The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. 
# Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

# Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

# Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

# Example 1:

# Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,1,0]]
# We erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,1,1,0]]
# The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
# [[1,0,0,0],
#  [0,0,0,0]]
# Hence the result is [2].
from typing import List
from collections import deque

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        result=[]
        directions=[[1,0],[0,1],[0,-1]]

        for idx in range(len(hits)):
            curr_erase=hits[idx]
            grid[curr_erase[0]][curr_erase[1]]=0
            unstableCount=0

            stableBricks=deque()
            visited=set()
            for j in range(len(grid[0])):
                visited.add((0,j))
                if grid[0][j]!=0:
                    stableBricks.append((0,j))
            while stableBricks:
                curr_i,curr_j=stableBricks.popleft()
                grid[curr_i][curr_j]+=1
                for ix,jx in directions:
                    next_i,next_j=curr_i+ix,curr_j+jx
                    if 0<=next_i<len(grid) and 0<=next_j<len(grid[0]) and (next_i,next_j) not in visited and grid[next_i][next_j]==grid[curr_i][curr_j]-1:
                        visited.add((next_i,next_j))
                        stableBricks.append((next_i,next_j))
            print(grid)
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==idx+1:
                        unstableCount+=1
            
            result.append(unstableCount)

        return result

# ============================================================
# REVERSE SIMULATION VARIANT
# ============================================================

# 803. Bricks Falling When Hit - Reverse Simulation Approach
# https://leetcode.com/problems/bricks-falling-when-hit/description/

from typing import List
from collections import deque

class SolutionReverseSimulation:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        Reverse simulation: Process hits backward.
        When we restore a brick, count newly connected bricks.
        This equals bricks that fell when erased (forward direction).
        """
        m, n = len(grid), len(grid[0])

        # Step 1: Track which bricks exist and which are hit
        bricks = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bricks[i][j] = True

        # Step 2: Apply all hits upfront (remove hit bricks)
        for r, c in hits:
            bricks[r][c] = False

        result = [0] * len(hits)

        # Step 3: Helper function to find all stable bricks using BFS from top
        def get_stable_bricks():
            """Returns set of bricks connected to the top"""
            visited = set()
            queue = deque()

            # Start BFS from top row
            for j in range(n):
                if bricks[0][j]:
                    queue.append((0, j))
                    visited.add((0, j))

            # BFS: explore all connected bricks
            while queue:
                i, j = queue.popleft()

                # Check 3 directions: down, right, left (no need for up in this context)
                for di, dj in [(1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                        if bricks[ni][nj]:
                            visited.add((ni, nj))
                            queue.append((ni, nj))

            return visited

        # Step 4: Process hits in reverse order
        stable_bricks = get_stable_bricks()

        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]

            # Restore (un-erase) the brick
            bricks[r][c] = True

            # OPTIMIZATION: Check if restored brick can become stable
            # If it's at the top or adjacent to a stable brick, it will be stable
            is_at_top = (r == 0)
            is_adjacent_to_stable = any(
                (r + dr, c + dc) in stable_bricks
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            )

            if is_at_top or is_adjacent_to_stable:
                # Run BFS only if the restored brick can become stable
                new_stable_bricks = get_stable_bricks()

                # Count how many OTHER bricks became stable
                newly_stable = new_stable_bricks - stable_bricks
                newly_stable.discard((r, c))  # Remove the brick itself from count

                result[i] = len(newly_stable)

                # Update for next iteration
                stable_bricks = new_stable_bricks
            else:
                # Restored brick is isolated, nothing changes
                result[i] = 0

        return result

# ============================================================
# UNION-FIND VARIANT
# ============================================================

# 803. Bricks Falling When Hit - Union-Find Solution
# https://leetcode.com/problems/bricks-falling-when-hit/description/

from typing import List

class SolutionUnionFind:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        Union-Find approach: Process hits in reverse.
        Track connected components to the top using union-find.
        """
        m, n = len(grid), len(grid[0])

        # ===== UNION-FIND DATA STRUCTURE =====
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))  # Each node is initially its own parent
                self.size = [1] * size           # Each component has size 1 initially

            def find(self, x):
                """Find the root (representative) of x's component with path compression"""
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Compress path
                return self.parent[x]

            def union(self, x, y):
                """
                Merge components of x and y.
                Returns the number of bricks that got added to x's component.
                """
                px, py = self.find(x), self.find(y)

                # Already in same component
                if px == py:
                    return 0

                # Union by rank: attach smaller tree to larger tree
                if self.size[px] < self.size[py]:
                    px, py = py, px

                self.parent[py] = px
                self.size[px] += self.size[py]
                return self.size[py]  # Return size that was merged

            def get_size(self, x):
                """Get the size of the component containing x"""
                return self.size[self.find(x)]

        # ===== MAIN ALGORITHM =====
        # Create union-find with m*n bricks + 1 virtual "TOP" node
        uf = UnionFind(m * n + 1)
        top = m * n  # Virtual node representing "connected to top"

        # Track which brick positions are present (not erased)
        is_present = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    is_present[i][j] = True

        # Step 1: Apply all hits (erase those bricks)
        for r, c in hits:
            is_present[r][c] = False

        # Step 2: Pre-union all ADJACENT bricks to build connected components
        # Key insight: when we restore a brick, we merge entire components, not individual bricks
        for i in range(m):
            for j in range(n):
                if is_present[i][j]:
                    idx = i * n + j
                    # Union with right neighbor (don't need up due to grid traversal)
                    if j + 1 < n and is_present[i][j + 1]:
                        uf.union(idx, i * n + (j + 1))
                    # Union with down neighbor
                    if i + 1 < m and is_present[i + 1][j]:
                        uf.union(idx, (i + 1) * n + j)

        # Step 3: Connect all TOP-row bricks to the virtual TOP node
        for j in range(n):
            if is_present[0][j]:
                uf.union(top, 0 * n + j)

        result = [0] * len(hits)

        # Step 4: Process hits in REVERSE order
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            idx = r * n + c

            # Skip if the original grid had no brick here
            if grid[r][c] == 0:
                result[i] = 0
                continue

            # Get component size BEFORE restoring this brick
            size_before = uf.get_size(top)

            # Restore (un-erase) the brick
            is_present[r][c] = True

            # Union with all adjacent present bricks
            # Since we pre-unioned all bricks into components, this merges entire components
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # Check if neighbor is in bounds and present
                if 0 <= nr < m and 0 <= nc < n and is_present[nr][nc]:
                    n_idx = nr * n + nc
                    # Union with neighbor (merges components)
                    uf.union(idx, n_idx)

            # Connect to TOP if at top row or connected to TOP via neighbors
            if r == 0 or uf.find(idx) == uf.find(top):
                uf.union(idx, top)

            # Get component size AFTER restoring this brick
            size_after = uf.get_size(top)

            # Only count OTHER bricks that became stable (exclude the restored brick itself)
            # If the brick didn't join TOP, size_after == size_before, result = 0
            # If it did join TOP, subtract 1 to exclude itself
            result[i] = max(0, size_after - size_before - 1)

        return result

if __name__=="__main__":
    s=Solution()
    print(s.hitBricks([[1,0,0,0],[1,1,0,0]],[[1,1],[1,0]]))
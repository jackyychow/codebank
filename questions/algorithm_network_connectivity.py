# Source: Akuna
# Question: Find the minimum operations needed to connect a network.
#

"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
"""

# As long as there are at least (n - 1) connections, there is definitely a way to connect all computers.
# Use DFS to determine the number of isolated computer clusters.

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        visited=set()
        graph=defaultdict(list)

        for n1,n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for node in graph[curr]:
                if node not in visited:
                    dfs(node)
            return

        count=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count-1

        # Time O(connections)
        # Space O(n)
        
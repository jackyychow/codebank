# Source: Akuna
# Question: Find the minimum operations needed to connect all computers.
#

# As long as there are at least (n - 1) connections, there is definitely a way to connect all computers.
# Use DFS to determine the number of isolated computer clusters.
from collections import defaultdict

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

        countCluster=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                countCluster+=1

        return countCluster-1
        
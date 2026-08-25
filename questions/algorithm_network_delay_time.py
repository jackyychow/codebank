# Source: Akuna
# Question: Find the time for a signal to reach all nodes.
#

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        graph = defaultdict(list)

        for src, dest, duration in times:
            graph[src].append([dest, duration])

        heap = [[0, k]]

        while heap:
            time_elapsed, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            if len(visited) == n:
                return time_elapsed
            for neighbour_node, duration in graph[curr_node]:
                if neighbour_node not in visited:
                    heapq.heappush(heap, [time_elapsed + duration, neighbour_node])

        return -1

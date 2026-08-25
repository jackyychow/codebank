# Source: Akuna
# Question: Find the maximum star sum in a graph.
#

class Node:
    def __init__(self, val):
        self.summ = val
        self.heap = []

    def add(self, val, limit):
        if val <= 0 or limit == 0:
            return
        if len(self.heap) < limit:
            heapq.heappush(self.heap, val)
            self.summ += val
        else:
            if val > self.heap[0]:
                removed = heapq.heappushpop(self.heap, val)
                self.summ -= removed
                self.summ += val


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        maxSum = max(vals)
        graph = {}

        for n1, n2 in edges:
            if n1 not in graph:
                graph[n1] = Node(vals[n1])
            graph[n1].add(vals[n2], k)
            maxSum = max(maxSum, graph[n1].summ)
            if n2 not in graph:
                graph[n2] = Node(vals[n2])
            graph[n2].add(vals[n1], k)
            maxSum = max(maxSum, graph[n2].summ)

        return maxSum

# 
# class Solution:
#     def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
#         graph = defaultdict(set)
#         for i,j in edges:
#             if vals[i] > 0 : graph[j].add(i)
#             if vals[j] > 0 : graph[i].add(j)
            
#         stars = []
#         for i,v in enumerate(vals):
#             vv = [vals[j] for j in graph[i]]
#             vv.sort(reverse=True)
#             stars.append(v + sum(vv[0:k]))
            
#         return max(stars)
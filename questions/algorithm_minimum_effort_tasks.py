# Source: Akuna
# Question: Find the minimum initial energy needed to complete tasks.
#

from collections import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # We want to go through tasks in descending order of energy we could carry
        # over to the next task
        tasks.sort(key=lambda x: x[0] - x[1])
        
        curr_energy = 0
        borrowed = 0
        for i in range(len(tasks)):
            need = max(0, max(tasks[i]) - curr_energy)
            borrowed += need
            curr_energy = curr_energy + need - tasks[i][0]

        return borrowed

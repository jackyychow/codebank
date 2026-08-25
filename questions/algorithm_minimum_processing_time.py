# Source: Akuna
# Question: Assign tasks to processors to minimize completion time.
#

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()

        res = 0

        for i in range(len(tasks) // 4):
            res = max(res, processorTime[i] + tasks[3 + (i * 4)])

        return res
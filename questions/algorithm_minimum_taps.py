# Source: Akuna
# Question: Find the minimum taps needed to water a garden.
#

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        max_reach = [0] * (n + 1)
        # max_reach[i] is the furthest right point i-th tap can reach

        for i, current_range in enumerate(ranges):
            left = max(0, i - current_range)
            right = min(n, i + current_range)
            max_reach[left] = max(max_reach[left], right)

        taps_needed = 0
        current_reach = 0
        next_reach = 0

        for i in range(n):
            # If we can't advance, the garden can't be watered.
            if next_reach <= i and max_reach[i] == i:
                return -1

            next_reach = max(next_reach, max_reach[i])

            # When current reach equals i, we must open a tap
            if current_reach == i:
                taps_needed += 1
                current_reach = next_reach

        return taps_needed
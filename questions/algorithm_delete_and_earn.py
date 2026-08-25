# Source: Akuna
# Question: Maximize points under delete-and-earn constraints.
#

# What is the range of values for the integers in the input array? Can they be negative?
# Can the input array be empty or null?
# If there are multiple occurrences of the same number, do I earn points for each occurrence when I delete it?
# Is there a specific ordering I need to consider when picking which numbers to delete first?
# Are there any constraints on the size of the input array?

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        dp = [0] * (max(nums) + 1)

        dp[0] = 0
        if 1 in count:
            dp[1] = count[1]

        for i in range(2, max(nums)+1):
            if i in count:
                dp[i] = max(dp[i - 1], dp[i - 2] + (i * count[i]))
            else:
                dp[i] = dp[i - 1]


        return dp[-1]

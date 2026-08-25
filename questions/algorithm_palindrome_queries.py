# Source: Akuna
# Question: Determine whether substrings can be rearranged into palindromes under replacements.
#

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []

        dp = [[0] * 26]
        for i in range(1, len(s) + 1):
            new = dp[i - 1][:]
            new[ord(s[i - 1]) - ord("a")] += 1
            dp.append(new)

        for start, end, limit in queries:
            L = dp[start]
            R = dp[end + 1]
            numOdds = sum((R[i] - L[i]) % 2 for i in range(26))
            # TLE
            # counter = Counter(s[start : end + 1])
            # numOdds = 0
            # for char in counter:
            #     if counter[char] % 2 == 1:
            #         numOdds += 1
            need = numOdds // 2
            res.append(need <= limit)

        return res
# Source: Tower Capital
# Question: Count structurally unique binary search trees.
#

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
# https://leetcode.com/problems/unique-binary-search-trees/description/

from functools import cache

class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        
        summ=0
        for i in range(n):
            summ+=self.numTrees(i)*self.numTrees(n-1-i)
        return summ
        

if __name__=="__main__":
    s=Solution()
    print(s.numTrees(5))
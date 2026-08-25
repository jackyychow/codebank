# Question: Find the length of the longest increasing subsequence.
#

class N2Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

class NLOGNSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [nums[0]]
        for num in nums:
            #if num is alredy in the list skip
            if num in l:
                continue
            #if nums is greater than the last element of the list(the max)
            #just append at the end of the list
            if num > l[-1]:
                l.append(num)
            else:
                #binary search of the smallest element of the list
                #that is greater than num
                s, e = 0, len(l)-1
                while e > s:
                    mid = s + (e-s)//2
                    if l[mid] < num:
                        s = mid + 1
                    else:
                        e = mid
                #swap num with the smallest element of the list that is greater than num
                l[e] = num
            # print(l)
        return len(l)
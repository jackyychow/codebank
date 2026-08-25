# Question: Find subsequences whose values sum to zero.
#

# for contiguous array, use prefix sum
def sum_to_zero(nums):
    results=set()
    nums.sort()

    def backtrack(idx, arr, curr_sum):
        if idx == len(nums):
            if curr_sum==0 and len(arr)>0:
                results.add(tuple(arr))
            return

        backtrack(idx+1, arr+[nums[idx]], curr_sum+nums[idx])
        backtrack(idx+1,arr,curr_sum)

    backtrack(0,[],0)
    
    return [list(t) for t in results]

if __name__=="__main__":
    print(sum_to_zero([-3,-2,-1,1,2,3]))
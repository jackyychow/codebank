# Question: Rearrange characters so equal characters are not adjacent.
#

#!/usr/bin/env python3
import heapq
from collections import Counter
# reorganize strings to no consecutive characters, return "" if impossible

def reorganizeString(s: str):
    result=""
    freq=Counter(s)
    max_heap=[]
    for k in freq:
        max_heap.append([-freq[k],k])

    heapq.heapify(max_heap)
    prev=heapq.heappop(max_heap)
    prev[0]+=1
    result+=prev[1]

    while max_heap:
        curr=heapq.heappop(max_heap)
        result+=curr[1]
        curr[0]+=1
        if prev[0]<0:
            heapq.heappush(max_heap,prev)
        prev=curr

    if prev[0]<0:
        return ""
# check prev before returning
    return result


if __name__ == "__main__":
    print(reorganizeString("jjjk"))
    print(reorganizeString("jjjka"))
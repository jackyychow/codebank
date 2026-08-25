# Question: Find the top K most frequent IP addresses in a file.
#

from collections import defaultdict
import heapq

def top_k_freq_ips(file_path, k):
    ip_count=defaultdict(int)

    with open(file_path, "r") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue

            ip = line.split()[0]
            ip_count[ip]+=1


    min_heap=[]
    for ip,count in ip_count.items():
        if len(min_heap)<k:
            heapq.heappush(min_heap, (count,ip))
        elif count>min_heap[0][0]:
            heapq.heapreplace(min_heap,(count,ip))


    min_heap.sort(lambda x: x[0],reverse=True)

    return [(ip,count) for count,ip in min_heap]


# Source: WorldQuant
# Question: Sort strings by the frequency of their anagram groups.
#

# Given an array of strings, sort the array based on the frequency of anagrams in descending order.
from collections import defaultdict
def convert_ascii(s):
    lst=[0 for _ in range(26)]
    for char in s:
        lst[ord(char)-ord('a')]+=1
    return tuple(lst)
        
def anagram_freq(arr):
    freq=defaultdict(int)
    for s in arr:
        freq[convert_ascii(s)]+=1
    arr.sort(key=lambda x: (-freq[convert_ascii(x)], x))
    return arr
    
if __name__=="__main__":
    print(anagram_freq(["eat", "tea", "tan", "ate", "nat", "bat", "ate"]))
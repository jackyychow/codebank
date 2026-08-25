# Source: Akuna
# Question: Implement a map supporting prefix-sum queries.
#

"""
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
"""

class Trie:
    def __init__(self, val=0):
        self.children = {}
        self.val = val
        self.vocab = {}


class MapSum:
    def __init__(self):
        self.head = Trie()

    def insert(self, key: str, val: int) -> None:
        curr = self.head
        for c in key:
            if c not in curr.children:
                curr.children[c] = Trie(val)
            else:
                if key in curr.children[c].vocab:
                    curr.children[c].val -= curr.children[c].vocab[key]
                curr.children[c].val += val
            curr.children[c].vocab[key] = val
            curr = curr.children[c]

    def sum(self, prefix: str) -> int:
        curr = self.head
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]

        return curr.val

# class MapSum(object):
    # def __init__(self):
    #     self.map = {}
    #     self.score = collections.Counter()

    # def insert(self, key, val):
    #     delta = val - self.map.get(key, 0)
    #     self.map[key] = val
    #     for i in xrange(len(key) + 1):
    #         prefix = key[:i]
    #         self.score[prefix] += delta

    # def sum(self, prefix):
    #     return self.score[prefix]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
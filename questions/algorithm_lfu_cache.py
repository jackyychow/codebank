# Source: Akuna
# Question: Implement an LFU cache with LRU tie-breaking.
#

from collections import defaultdict, OrderedDict
import unittest

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key->(value,freq)
        # self.key_to_val = {}
        # self.key_to_freq = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        """Return value and bump frequency; -1 if missing.

        Moves the key from its current frequency bucket to the next
        higher bucket and maintains `min_freq` when the old bucket empties.
        """
        if key not in self.cache:
            return -1

        value, freq = self.cache[key]
        
        # Remove from current freq bucket
        del self.freq_map[freq][key]

        # If this was min_freq and now empty, increment min_freq
        if not self.freq_map[freq] and freq==self.min_freq:
            self.min_freq+=1

        new_freq=freq+1
        self.freq_map[new_freq][key]=None
        self.cache[key]=(value,new_freq)

        return value

    def put(self, key: int, value: int) -> None:
        """Insert/update key; evict LFU (LRU tie-break) on capacity.

        On update, reuse `get` to centralize frequency bump logic.
        On insert, set `min_freq` to 1 and add to the 1-frequency bucket.
        """
        if self.capacity <= 0:
            return

        # If key exist
        if key in self.cache:
            _, freq = self.cache[key]
            self.cache[key]=(value,freq)
            self.get(key) #reuse get logic to update freq
            return

        if len(self.cache) >= self.capacity:
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[evict_key]

        self.cache[key] = (value,1)
        self.min_freq = 1
        self.freq_map[self.min_freq][key] = None

if __name__ == "__main__":
    # Simple smoke test
    # c = LFUCache(2)
    # c.put(1, 1)
    # c.put(2, 2)
    # assert c.get(1) == 1
    # c.put(3, 3)  # evicts 2
    # assert c.get(2) == -1
    # assert c.get(3) == 3
    # c.put(4, 4)  # evicts 3
    # assert c.get(3) == -1
    # assert c.get(4) == 4

    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1)==1  # returns 1, freq of 1 becomes 2
    lfu.put(3, 3)      # evicts key 2 (used once), adds key 3
    assert lfu.get(2)==-1  # returns -1 (not found)
    assert lfu.get(3)==3  # returns 3
    print("LFUCache smoke test passed")


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None) # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node
        
class LFUCacheDLL:
    def __init__(self, capacity):
        """
        :type capacity: int
        
        Three things to maintain:
        
        1. a dict, named as `self._node`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.
           
        2. Each frequency has a doubly linked list, store in `self._freq`, where key
           is the frequency, and value is an object of `DLinkedList`
        
        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
		   two rules:
           
           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.
           
           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)
           
        """
        self._size = 0
        self._capacity = capacity
        
        self._node = dict() # key: Node
        self._freq = defaultdict(DLinkedList)
        self._minfreq = 0
        
        
    def _update(self, node):
        """ 
        This is a helper function that used in the following two cases:
        
            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.
         
        The common point of these two cases is that:
        
            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change
        
        The logic of this function is:
        
            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minfreq is `f`,
               update self._minfreq to `f+1`
        
        All of the above opeartions took O(1) time.
        """
        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
    
    def get(self, key):
        """
        Through checking self._node[key], we can get the node in O(1) time.
        Just performs self._update, then we can return the value of node.
        
        :type key: int
        :rtype: int
        """
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.
        
        Otherwise, the following logic will be performed
        
        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self._node
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1
        
        (*) How to pop the least frequently used item? Two facts:
        
        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)
          
        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
                         recently used one, pop it...
        
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1


class TestLFUCache(unittest.TestCase):
    """Unit tests for both LFU implementations."""

    def test_basic_sequence_simple(self) -> None:
        """Basic put/get and LFU eviction for dict+OrderedDict variant."""
        c = LFUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), 1)
        c.put(3, 3)  # evicts 2
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(3), 3)
        c.put(4, 4)  # evicts 1
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(4), 4)

    def test_updates_and_minfreq_simple(self) -> None:
        """Update value keeps correct frequency behavior and min_freq bumping."""
        c = LFUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        c.put(1, 10)  # update
        self.assertEqual(c.get(1), 10)
        c.put(3, 3)  # evicts 2
        self.assertEqual(c.get(2), -1)

    def test_zero_capacity_simple(self) -> None:
        """Capacity 0 stores nothing."""
        c = LFUCache(0)
        c.put(1, 1)
        self.assertEqual(c.get(1), -1)

    def test_basic_sequence_dll(self) -> None:
        """Basic put/get and LFU eviction for DLL-based variant."""
        c = LFUCacheDLL(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), 1)
        c.put(3, 3)  # evicts 2
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(3), 3)
        c.put(4, 4)  # evicts 1
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(4), 4)

    def test_zero_capacity_dll(self) -> None:
        """Capacity 0 stores nothing for DLL variant."""
        c = LFUCacheDLL(0)
        c.put(1, 1)
        self.assertEqual(c.get(1), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
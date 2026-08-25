# Source: Akuna
# Question: Implement an LRU cache.
#

from typing import Any, Optional, Iterator, Tuple
from collections import OrderedDict
import unittest
import threading

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

    
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        # self.lock = threading.Lock()

        self.tail, self.head = Node(0, 0), Node(0, 0)
        self.tail.next, self.head.prev = self.head, self.tail

    # remove node from list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def _insert(self, node):
        prev, nxt = self.head.prev, self.head
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        # with self.lock:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # with self.lock:
        if key in self.cache:
            self._remove(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.tail.next
            self._remove(lru)
            del self.cache[lru.key]

class LRUCacheWithOrderedDict:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: Any) -> Any:
        if key not in self.cache:
            return -1
        # Move to the right end (most recent)
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: Any, value: Any) -> None:
        if key in self.cache:
             self.cache.move_to_end(key, last=True)
        self.cache[key] = value
        # Move updated or newly inserted key to the right end
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class TestLRUCache(unittest.TestCase):
    """Unit tests for the manual doubly-linked list LRUCache."""

    def test_basic_sequence(self) -> None:
        """Validates typical get/put sequence and LRU eviction order."""
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)  # evicts key 2
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)  # evicts key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_edge_cases(self) -> None:
        """Checks zero capacity, updates, and recency-driven eviction."""
        c0 = LRUCache(0)
        c0.put("a", 1)
        self.assertEqual(c0.get("a"), -1)

        c1 = LRUCache(1)
        c1.put("x", 1)
        c1.put("x", 2)  # update
        self.assertEqual(c1.get("x"), 2)

        c2 = LRUCache(2)
        c2.put("a", 1)
        c2.put("b", 2)
        self.assertEqual(c2.get("a"), 1)  # makes 'a' MRU
        c2.put("c", 3)  # evicts 'b'
        self.assertEqual(c2.get("b"), -1)


class TestLRUCacheWithOrderedDict(unittest.TestCase):
    """Unit tests for the OrderedDict-based LRU implementation."""

    def test_basic_sequence(self) -> None:
        """Validates typical sequence and correct OrderedDict eviction semantics."""
        cache = LRUCacheWithOrderedDict(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_edge_cases(self) -> None:
        """Checks zero capacity and updates with OrderedDict variant."""
        c0 = LRUCacheWithOrderedDict(0)
        c0.put("a", 1)
        self.assertEqual(c0.get("a"), -1)

        c1 = LRUCacheWithOrderedDict(1)
        c1.put("x", 1)
        c1.put("x", 2)
        self.assertEqual(c1.get("x"), 2)

        c2 = LRUCacheWithOrderedDict(2)
        c2.put("a", 1)
        c2.put("b", 2)
        self.assertEqual(c2.get("a"), 1)
        c2.put("c", 3)
        self.assertEqual(c2.get("b"), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
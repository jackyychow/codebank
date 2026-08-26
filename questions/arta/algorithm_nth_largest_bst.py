# Question: Find the nth-largest value in a binary search tree.
#
# Reverse in-order traversal visits values from largest to smallest.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeTraversal:
    def findNthLargest(self, root, n):
        count = n

        def traverse(node):
            nonlocal count
            if not node:
                return None
            right = traverse(node.right)
            if right:
                return right
            count -= 1
            if count == 0:
                return node.val
            left = traverse(node.left)
            return left

        return traverse(root)


if __name__ == "__main__":
    root = Node(3, Node(1), Node(5, Node(4), Node(6)))
    tree = TreeTraversal()
    assert tree.findNthLargest(root, 1) == 6
    assert tree.findNthLargest(root, 4) == 3

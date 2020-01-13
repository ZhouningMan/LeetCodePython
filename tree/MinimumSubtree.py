"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

MAX_INT = 2 ** 63 - 1
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        node, _, _ = self.min_sum(root)
        return node

    def min_sum(self, root):
        if root is None:
            return None, 0, MAX_INT
        left, left_sum, left_min = self.min_sum(root.left)
        right, right_sum, right_min = self.min_sum(root.right)
        curr_sum = left_sum + right_sum + root.val
        if left is None and right is None:
            entries = [(root, curr_sum)]
        elif left is None:
            entries = [(root, curr_sum), (right, right_min)]
        elif right is None:
            entries = [(root, curr_sum), (left, left_min)]
        else:
            entries = [(root, curr_sum), (left, left_min), (right, right_min)]
        node, curr_min = min(entries, key=lambda entry: entry[1])
        return node, curr_sum, curr_min

    def min_sum_simplified(self, root):
        if root is None:
            return None, 0, MAX_INT
        left, left_sum, left_min = self.min_sum(root.left)
        right, right_sum, right_min = self.min_sum(root.right)
        curr_sum = left_sum + right_sum + root.val
        entries = [(root, curr_sum), (left, left_min), (right, right_min)]
        node, curr_min = min(entries, key=lambda entry: entry[1])
        return node, curr_sum, curr_min
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        if root is None:
            return root
        return self.max_average(root)[0]

    def max_average(self, node):
        if node is None:
            return node, -2**63, 0, 0
        left_node, left_max, left_sum, left_count = self.max_average(node.left)
        right_node, right_max, right_sum, right_count = self.max_average(node.right)
        curr_sum = left_sum + right_sum + node.val
        curr_count = left_count + right_count + 1
        average = curr_sum / curr_count
        if average >= left_max and average >= right_max:
            return node, average, curr_sum, curr_count
        elif left_max >= average and left_max >= right_max:
            return left_node, left_max, curr_sum, curr_count
        else:
            return right_node, right_max, curr_sum, curr_count

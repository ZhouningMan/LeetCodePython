"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

MAX_INT = 2**63 - 1
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        node, _ = self.helper(root, target)
        return node.val

    def helper(self, root, target):
        if not root:
            return None, MAX_INT
        if target == root.val:
            return root, 0
        currD = abs(root.val - target)
        next = root.left if root.val > target else root.right
        child, childD = self.helper(next, target)
        if currD <= childD:
            return root, currD
        else:
            return child, childD




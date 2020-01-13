"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        valid, _ = self.helper(root)
        return valid


    def helper(self, root):
        if not root:
            return True, 0
        l_valid, l_hei = self.helper(root.left)
        if not l_valid:
            return False, -1
        r_valid, r_hei = self.helper(root.right)
        if not r_valid:
            return False, -1
        if abs(l_hei - r_hei) > 1:
            return False, -1
        return True, max(l_hei, r_hei) + 1


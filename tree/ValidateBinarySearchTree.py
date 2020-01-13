"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
MIN_INT = -2**63
MAX_INT = 2**63 - 1

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        valid, _, _ = self.isvalid(root)
        return valid

    def isvalid(self, root):
        if root is None:
            return True, None, None
        left_valid, left_min, left_max = self.isvalid(root.left)
        if not left_valid:
            return False, None, None
        right_valid, right_min, right_max = self.isvalid(root.right)
        if not right_valid:
            return False, None, None
        if left_max is not None and left_max >= root.val:
            return False, None, None
        if right_min is not None and root.val >= right_min:
            return False, None, None
        min_val = left_min if left_min is not None else root.val
        max_val = right_max if right_max is not None else root.val
        return True, min_val, max_val

    def isValidBST_Iterative(self, root):
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if pre and pre.val >= node.val:
                return False
            pre = node
            root = node.right
        return True
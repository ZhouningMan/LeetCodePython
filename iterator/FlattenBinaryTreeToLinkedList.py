"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        return self._flatten_sub(root, None)

    # add the tail to the flattened root
    # return the new head
    def _flatten_sub(self, root, tail):
        if root is None:
            return tail
        # flattened right with the tail append to the end of the right tree
        flattend_right = self._flatten_sub(root.right, tail)
        # flatten left and then assign it to the right subtree
        root.right = self._flatten_sub(root.left, flattend_right)
        # nullify left
        root.left = None
        # return new head
        return root

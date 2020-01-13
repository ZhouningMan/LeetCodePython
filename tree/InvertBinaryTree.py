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
    def invertBinaryTree(self, root):
        self.invert(root)

    def invert(self, root):
        if root is None:
            return root
        left = self.invert(root.left)
        right = self.invert(root.right)
        root.left = right
        root.right = left
        return root

    def invert_iterative(self, root):
        stack = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            # Each pop indicates an event we need to process
            # it is similar to the real work in an recursive algorithm
            # the work here is to swap the left and right subtree
            root = stack.pop()
            right = root.right
            # swap left and right
            root.left, root.right = root.right, root.left
            # we want to remember the previous right subtree
            # and we start working on right subtree
            root = right
        return root

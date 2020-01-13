"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result

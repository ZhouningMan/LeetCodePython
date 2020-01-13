"""
        1
    2       3
  4    5

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return self.dfs(root, 0)

    def dfs(self, root, height):
        if not root.left and not root.right:
            return None, height
        if root.left and root.right:
            left_anc, left_hi = self.dfs(root.left, height + 1)
            right_anc, right_hi = self.dfs(root.right, height + 1)
            if left_hi == right_hi == height + 1:
                return root, height
            return (left_anc, left_hi) if left_hi > right_hi else (right_anc, right_hi)
        if root.left:
            left_anc, left_hi = self.dfs(root.left, height + 1)
            return (left_anc, left_hi) if left_hi > height + 1 else (root, height)
        if root.rigth:
            right_anc, right_hi = self.dfs(root.right, height + 1)
            return (right_anc, right_hi) if right_hi > height + 1 else (root, height)

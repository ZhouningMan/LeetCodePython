# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, 0)[0]

    # return the common ancestor and the depth of the deepest leaf node under its control
    def dfs(self, root, depth):
        if not root:
            return None, depth
        lnode, lhi = self.dfs(root.left, depth + 1)
        rnode, rhi = self.dfs(root.right, depth + 1)
        if lhi == rhi:
            return root, lhi
        elif lhi > rhi:
            return lnode, lhi
        else:
            return rnode, rhi

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return self.dfs(root, 0)[0]

    def dfs(self, root, height):
        if not root:
            return None, height
        height += 1
        lca, left_hi = self.dfs(root.left, height)
        rca, right_hi = self.dfs(root.right, height)
        # if left and right subtree has the same depth,
        # the this node is the common ancestor for let and right
        if left_hi == right_hi:
            # we want to remember the deepest depth
            return root, left_hi
        elif left_hi > right_hi:
            return lca, left_hi
        else:
            return rca, right_hi
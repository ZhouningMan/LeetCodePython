"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        common, _, _ = self.helper(root, A, B)
        return common

    def helper(self, root, A, B):
        if root is None:
            return None, False, False
        lca, lHasA, lHasB = self.helper(root.left, A, B)
        if lca:
            return lca, True, True
        rca, rHasA, rHasB= self.helper(root.right, A, B)
        if rca:
            return rca, True, True
        # does the current subtree contains A
        hasA = lHasA or rHasA or root is A
        # does the current subtree contains B
        hasB = lHasB or rHasB or root is B
        # if current subtree contains both A and B, then it is a common
        # ancestor, because we are doing bottom up, the first solution
        # is the lowest common ancestor
        common = root if hasA and hasB else None
        return common, hasA, hasB



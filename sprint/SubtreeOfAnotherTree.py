# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        svalues = []
        self.preorder(s, svalues)
        tvalues = []
        self.preorder(t, tvalues)
        # we cannot just simply join by "," because
        # casess like root(12) and root(2)
        return "".join(tvalues) in "".join(svalues)

    def preorder(self, root, values):
        if not root:
            # we need to maintain the structure, we cannot ignore null node
            # need to add special character to indicate its structure
            values.append(",#")
            return
        values.append("," + str(root.val))
        self.preorder(root.left, values)
        self.preorder(root.right, values)
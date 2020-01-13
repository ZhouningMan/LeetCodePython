"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        stack = []
        matched = False
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if matched:
                return node
            if node is p:
                matched = True
            root = node.right
        return None

    def inorderSuccessor2(self, root, p):
        if not root:
            return None
        if p.right: # find the next biggest
            p = p.right
            while p.left:
                p = p.left
            return p

        path = []
        # path contains nodes that are greater than p
        self.helper2(root, p, path)
        if len(path) < 2:
            return None
        return path[-2]

    def helper2(self, root, p, path):
        path.append(root)
        if root is p:
            return
        if p.val < root.val:
            return self.helper2(root.left, p, path)
        else:
            # if we go right, that means, parent node is smaller than us
            path.pop()
            return self.helper2(root.right, p, path)


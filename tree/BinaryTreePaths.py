"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []
        paths = []
        self.all_paths(paths, [], root)
        return paths

    def all_paths(self, paths, path, node):
        path.append(str(node.val))  # python is strict about type
        if node.left is None and node.right is None:
            paths.append('->'.join(path))
            path.pop()  # remember to pop on this exit place
            return
        if node.left is not None:
            self.all_paths(paths, path, node.left)
        if node.right is not None:
            self.all_paths(paths, path, node.right)
        path.pop()  # pop the value


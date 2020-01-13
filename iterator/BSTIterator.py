"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        left = root
        # go to left subtree
        while left:
            self.stack.append(left)
            left = left.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self, ):
        node = self.stack.pop()
        # this is where we visited the node
        # same as in order traversal
        child = node.right

        # visits right subtree
        while child:
            self.stack.append(child)
            child = child.left
        return node
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        deq = deque([root])
        go_right = True  # current level direction
        result = []
        while deq:
            next_lvl = deque()
            level = []
            while deq:
                # because this is zig zag order, the deq is always act as a stack
                node = deq.pop()
                if not node:
                    continue
                level += [node.val]
                # if current level go right, then first append left, than right
                if go_right:
                    next_lvl += [node.left, node.right]
                # if current level go left, then first append right, then left
                else:
                    next_lvl += [node.right, node.left]
            deq = next_lvl
            if level:
                result.append(level)
            go_right = not go_right
        return result
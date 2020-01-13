# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([root])
        level = 0
        complete = True
        while queue:
            # if we have seen incomplete row, we saw it again
            if not complete:
                return False
            size = len(queue)
            complete = size == 2 ** level
            bothChildren = True
            for i in range(size):
                node = queue.popleft()
                if node.right and not node.left:
                    return False
                # only one node might not have both children
                if not bothChildren and (node.left or node.right):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                bothChildren = node.left and node.right
            level += 1
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    def btreeGameWinningMove(self, root, n, x):
        countMap = defaultdict(int)
        node = self.find(root, x)
        # i need to remember the root, because that value is not remembered during the traversal
        countMap[root] = self.count(root, countMap, node)
        maxCount = max(countMap[root] - countMap[node],  # total counts of chosing parent
                       countMap[node.left],
                       countMap[node.right])

        return maxCount > n // 2

    def find(self, root, x):
        if not root:
            return None
        if root.val == x:
            return root
        left = self.find(root.left, x)
        return left if left else self.find(root.right, x)

    def count(self, root, countMap, node):
        if not root:
            return 0
        total = 1 + self.count(root.left, countMap, node) + self.count(root.right, countMap, node)
        if root is node or root is node.left or root is node.right:
            countMap[root] = total
        return total
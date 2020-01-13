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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            size = len(queue)  # size of this level
            for i in range(size):
                head = queue.popleft()  # pop the head
                level.append(head.val)
                # do something with the head
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            result += [level]
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    res = s.levelOrder(root)
    print(res)
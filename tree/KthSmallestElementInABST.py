"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        ans, _ = self.helper(root, k)
        return ans.val

    # return the result, distance away from the correct node
    def helper(self, root, k):
        if root is None:
            return None, k
        left, lk = self.helper(root.left, k)
        if left:
            return left, 0
        if lk == 1:  # in order traversal
            return root, 0
        right, rk = self.helper(root.right, lk - 1)
        if right:
            return right, 0
        return None, rk

    def kthSmallest_iterative(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            root = node.right
        return None

if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)),TreeNode(4)), TreeNode(6))
    s = Solution()
    ans = s.kthSmallest(tree, 3)
    print(ans)
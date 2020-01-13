"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []
        ans = []
        queue = deque([root])  # all queue elements are not none
        while queue:
            m = len(queue)
            # virtual head of the list
            li = ListNode(-1)
            curr = li
            for i in range(m):
                head = queue.popleft()
                curr.next = ListNode(head.val)
                # don't forget to advance list iterator
                curr = curr.next
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            ans.append(li.next)
        return ans


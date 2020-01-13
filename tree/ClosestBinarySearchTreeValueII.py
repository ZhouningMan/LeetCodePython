# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def closestKValues(self, root, target, k):
        smaller = []  # the stack that keeps that values smaller than target
        bigger = []  # the stack that keeps the values bigger than target logn space
        curr = root
        # initialize both stacks
        while curr:
            if curr.val <= target:
                smaller.append(curr)
                curr = curr.right
            else:
                bigger.append(curr)
                curr = curr.left
        ans = []
        while k > 0:
            if not smaller:
                ans += [self.get_bigger(bigger)]
            elif not bigger:
                ans += [self.get_smaller(smaller)]
            # the top of the stacks are cloest to the target
            elif target - smaller[-1].val < bigger[-1].val - target:
                ans += [self.get_smaller(smaller)]
            else:
                ans += [self.get_bigger(bigger)]
            k -= 1
        return ans

    # very interesting algorithm to keep them in order
    def get_bigger(self, bigger):
        ans = bigger.pop()
        node = ans.right
        while node:  # logn
            bigger += [node]
            node = node.left
        return ans.val

    def get_smaller(self, smaller):
        ans = smaller.pop()
        node = ans.left
        while node:  # logn
            smaller.append(node)
            node = node.right
        return ans.val
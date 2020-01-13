"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        if not A or len(A) == 0:
            return None
        nodes = {}
        for num in A:  # create nodes
            nodes[num] = TreeNode(num)

        stack = [-1] # Add a imaginary biggest left
        # the key to this problem is t
        for i, val in enumerate(A):
            # since we are building monotonously decreasing stack
            # so we know immediate the value greater
            # than the current value on the left and rights
            while len(stack) > 1 and A[stack[-1]] < val:
                child_idx = stack.pop()
                child_val = A[child_idx]
                # parent index for child_idx is either stack[-1] or i
                left_greater = sys.maxsize if stack[-1] == -1 else A[stack[-1]]
                if left_greater > val:
                    # val is the parent value
                    nodes[val].left = nodes[child_val]
                else:
                    # left value is the parent value
                    nodes[left_greater].right = nodes[child_val]
            stack.append(i)

        while len(stack) > 2:  # we want to ignore first element as that is imaginary
            child_idx = stack.pop()
            nodes[A[stack[-1]]].right = nodes[A[child_idx]]
        return nodes[A[stack[-1]]]


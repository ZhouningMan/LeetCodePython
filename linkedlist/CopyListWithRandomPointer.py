"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        visited = {}
        curr = head
        while curr:
            copy = self.get_or_insert(visited, curr)
            nn = self.get_or_insert(visited, curr.next)
            rn = self.get_or_insert(visited, curr.random)
            copy.next = nn
            copy.random = rn
            curr = curr.next
        return visited[head]

    def get_or_insert(self,visited, node):
        if not node:
            return None
        if node in visited:
            return visited[node]
        else:
            copy = RandomListNode(node.label)
            visited[node] = copy
            return copy
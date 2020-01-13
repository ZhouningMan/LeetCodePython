"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque

class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        ans = []
        visited = set()
        for node in nodes:
            if node not in visited:
                ans.append(self.bfs(node, visited))
        return ans

    def bfs(self, node, visited):
        visited.add(node)
        queue = deque([node])
        # DO NOT do cc = [node.label]
        # since we are handling adding the node to cc within first loop
        cc = []
        while queue:
            head = queue.popleft()
            cc.append(head.label)
            for nb in head.neighbors:
                if nb in visited:
                    continue
                visited.add(nb)
                queue.append(nb)
        return list(sorted(cc))
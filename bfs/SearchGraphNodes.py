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
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        if values[node] == target:
            return node
        visited = {node}
        queue = deque([node])

        while queue:
            head = queue.popleft()
            for nb in head.neighbors:
                if nb in visited:
                    continue
                if values[nb] == target:
                    return nb
                queue.append(nb)
                visited.add(nb)
        return None

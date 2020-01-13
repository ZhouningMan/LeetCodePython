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
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph2(self, node):
        if not node:
            return None
        # this doesn't pass the tests. 
        root = UndirectedGraphNode(node.label)
        queue = deque([node])
        clone_map = {node: root}
        visited = set()
        visited.add(node)
        while queue:
            node = queue.popleft()
            clone = clone_map[node]
            for ne in node.neighbors:
                # clone a node
                if ne not in clone_map:
                    ne_clone = UndirectedGraphNode(ne.label)
                    clone_map[ne] = ne_clone
                # establish the relationship
                clone.neighbors.append(clone_map[ne])
                if ne not in visited:
                    queue.append(ne)
                    visited.add(ne)
        return clone_map[node]

    def cloneGraph(self, node):
        if not node:
            return None
        clone_map = self.clone_nodes(node)
        # we need a deque
        queue = deque([node])
        # we need to add initial node visited set
        visited = {node}
        while queue:
            head = queue.popleft()
            new_head = clone_map[head]
            for ne in head.neighbors:
                new_head.neighbors.append(clone_map[ne])
                if ne not in visited:
                    queue.append(ne)
                    # every node in the queue must be in visited set
                    visited.add(ne)
        return clone_map[node]

    def clone_nodes(self, node):
        clone_map = {node: UndirectedGraphNode(node.label)}
        queue = deque([node])
        while queue:
            head = queue.popleft()
            for ne in head.neighbors:
                if ne not in clone_map:
                    clone_map[ne] = UndirectedGraphNode(ne.label)
                    queue.append(ne)
        return clone_map



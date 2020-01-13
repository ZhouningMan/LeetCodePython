"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
from collections import defaultdict

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSortBFS(self, graph):
        if not graph:
            return []
        node_indegrees = self.get_indegree(graph)
        queue = deque()
        visited = set()
        # initialize
        for node, v in node_indegrees.items():
            if v == 0:
                queue.append(node)
                visited.add(node)
        ans = []
        while queue:
            head = queue.popleft()
            ans.append(head)
            for ne in head.neighbors:
                if ne in visited:
                    continue
                node_indegrees[ne] -= 1
                if node_indegrees[ne] == 0:
                    queue.append(ne)
                    visited.add(ne)
        return ans

    def get_indegree(self, graph):
        # defaultdict is still required for neighbor
        indegrees = defaultdict(int)
        for node in graph:
            # we need to add each node in the map
            if node not in indegrees:
                indegrees[node] = 0
            for ne in node.neighbors:
                indegrees[ne] += 1
        return indegrees

    def topSortDFS(self, graph):
        if not graph:
            return []
        visited = set()
        postorder = []
        for node in graph:
            if node not in visited:
                self.dfs(node, visited, postorder)
        # we need to return reversed post order
        return list(reversed(postorder))

    def dfs(self, node, visited, postorder):
        visited.add(node)
        for nb in node.neighbors:
            if nb in visited:
                continue
            self.dfs(nb, visited, postorder)
        postorder.append(node)
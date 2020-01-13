# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        if A == B:
            return 1
        squeue = deque([A])
        svisited = {A}
        equeue = deque([B])
        evisited = {B}
        dist = 0
        while squeue and equeue:
            dist += 1
            if self.advance(squeue, svisited, evisited):
                return dist
            dist += 1
            if self.advance(equeue, evisited, svisited):
                return dist
        return -1

    def advance(self, queue, visited, target):
        size = len(queue)
        for i in range(size):
            head = queue.popleft()
            for nb in head.neighbors:
                if nb in target:
                    return True
                if nb in visited:
                    continue
                queue.append(nb)
                visited.add(nb)
        return False
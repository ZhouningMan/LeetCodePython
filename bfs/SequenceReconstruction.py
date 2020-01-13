from collections import deque
from collections import defaultdict

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        if len(org) != len(graph):
            return False
        indegrees = self.get_indegrees(graph)
        return self.can_reconstuct(org, graph, indegrees)

    def can_reconstuct(self, org, graph, indegrees):
        queue = deque()
        visited = set()
        for node, v in indegrees.items():
            if v == 0:
                visited.add(node)
                queue.append(node)
        order = []
        while queue:
            if len(queue) != 1:
                return False
            head = queue.popleft()
            order.append(head)
            for nb in graph[head]:
                if nb in visited:
                    continue
                indegrees[nb] -= 1
                if indegrees[nb] == 0:
                    queue.append(nb)
        return order == org

    def build_graph(self, seqs):
        graph = {}
        for li in seqs:
            for i in li:
                graph[i] = []

        for li in seqs:
            for i in range(1, len(li)):
                graph[li[i-1]].append(li[i])
        return graph

    def get_indegrees(self, graph):
        indegrees = defaultdict(int)
        for node, nbs in graph.items():
            if node not in indegrees:
                indegrees[node] = 0
            for nb in nbs:
                indegrees[nb] += 1
        return indegrees
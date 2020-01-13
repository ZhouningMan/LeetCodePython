from collections import deque
from collections import defaultdict
import heapq

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = defaultdict(set)
        self.build_graph(words, graph, 0)
        indegrees= self.get_indegrees(graph)
        return self.top_order(indegrees, graph)

    def get_indegrees(self, graph):
        indegrees = defaultdict(int)
        for node, nbs in graph.items():
            # make sure indegrees contains all elements
            if node not in indegrees:
                indegrees[node] = 0
            for nb in nbs:
                indegrees[nb] += 1
        return indegrees

    def top_order(self, indegree, graph):
        queue = []
        visited = set()
        for c, v in indegree.items():
            if v == 0:
                visited.add(c)
                heapq.heappush(queue, c)
        order = []
        while queue:
            head = heapq.heappop(queue)
            order.append(head)
            for nb in graph[head]:
                if nb in visited:
                    continue
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    heapq.heappush(queue, nb)
                    visited.add(nb)
        if len(order) == len(graph):
            return "".join(order)
        else:
            return ""

    def build_graph(self, words, graph, i):
        m = len(words)
        if m == 0:
            return
        # add the first character to the graph so the graph
        # contains all characters
        if words[0][i] not in graph:
            graph[words[0][i]] = set()
        sublist = []
        if i + 1 < len(words[0]):
            sublist.append(words[0])
        # we are looping from 1, so how do we deal Surrounded Regions with 0th element
        # for recursion algorithm, we just need to deal with what to do for each iteration
        for j in range(1, m):
            c = words[j][i]
            if words[j][i] not in graph:
                graph[c] = set()
            if c != words[j-1][i]:
                graph[words[j-1][i]].add(c)
                self.build_graph(sublist, graph, i + 1)
                sublist = []
            # don't need to add word with no more characters to compare
            if i + 1 < len(words[j]):
                sublist.append(words[j])

        # when the loop exists, there is one final list we need to search
        self.build_graph(sublist, graph, i + 1)

if __name__ == '__main__':
    s = Solution()
    res = s.alienOrder(["wrt","wrf","er","ett","rftt"])
    print(res)
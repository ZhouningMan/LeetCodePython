import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self._build_graph(numCourses, prerequisites)
        stack = collections.deque()
        visited = [False for _ in range(numCourses)]
        for v in range(len(graph)):
            if not visited[v]:
                if not self._dfs(graph, stack, set(), visited, v):
                    return []
        return list(reversed(stack))

    def _build_graph(self, num, prereqs):
        graph = [[] for _ in range(num)]
        for dep in prereqs:
            graph[dep[1]].append(dep[0])
        return graph

    def _dfs(self, graph, stack, path, visited, v):
        visited[v] = True
        path.add(v)
        for i in graph[v]:
            if i in path:
                return False
            if not visited[i]:
                if not self._dfs(graph, stack, path, visited, i):
                    return False
        path.remove(v)  # backtrack
        stack.append(v)
        return True

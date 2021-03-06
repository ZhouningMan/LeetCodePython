from collections import deque
from collections import defaultdict

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        graph, indegrees = self.build_graph(prerequisites)
        visited = set()
        queue = deque()
        # because for this problem each node is just an integer
        # we need to loop through each node
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        count = 0
        while queue:
            head = queue.popleft()
            count += 1
            for nb in graph[head]:
                if nb in visited:
                    continue
                indegrees[nb] -= 1
                if indegrees[nb] == 0:
                    visited.add(nb)
                    queue.append(nb)
        return count == numCourses

    # build in degrees
    def build_graph(self, preqs):
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for c, p in preqs:
            graph[p].append(c)
            indegrees[c] += 1
        return graph, indegrees

if __name__ == '__main__':
    s = Solution()
    res = s.canFinish(2, [[1, 0]])
    print(res)
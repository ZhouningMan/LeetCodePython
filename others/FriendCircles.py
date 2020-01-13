import collections


class Solution:

    def findCircleNum(self, m) -> int:
        if not m or len(m) == 0:
            return 0
        friend_roots = [i for i in range(len(m))]
        length = len(m)
        result = length
        for r in range(length):
            for c in range(r, length):
                if m[r][c] == 1:
                    f1 = self.find(friend_roots, r)
                    f2 = self.find(friend_roots, c)
                    if f1 != f2:
                        # union them
                        friend_roots[f1] = f2
                        result -= 1
        return result

    def find(self, friend_roots, p):
        while friend_roots[p] != p:
            friend_roots[p] = friend_roots[friend_roots[p]]
            p = friend_roots[p]
        return p

    def findCircleNumDFS(self, m):
        if not m or len(m) == 0:
            return 0
        # we only need 1D list for undirected graph to represent each vertex
        visited = [False for _ in range(len(m))]
        count = 0
        for r in range(len(m)):
            if not visited[r]:
                self._dfs(m, visited, r)
                count += 1
        return count

    def _dfs(self, m, visited, r):
        visited[r] = True
        for c in range(len(m)):
            if m[r][c] == 1 and not visited[c]:
                self._dfs(m, visited, c)


    def findCircleNumBFS(self, m):
        if not m or len(m) == 0:
            return 0
        queue = collections.deque()
        visited = [False for _ in range(len(m))]
        count = 0
        for r in range(len(m)):
            if not visited[r]:
                queue.append(r)
                while queue:
                    first = queue.popleft()
                    for c in range(len(m)):  # for each neighbors
                        if m[first][c] == 1 and not visited[c]:
                            visited[c] = True
                            queue.append(c)
                count += 1
        return count
    

if __name__ == '__main__':
    Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]])

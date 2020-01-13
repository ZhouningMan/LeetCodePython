from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        if not start or not end or not dict:
            return 0
        # we need to add the end word into the dictionary
        dict.add(end)
        queue = deque([start])
        visited = {start}
        path = 1
        while queue:
            m = len(queue)
            for i in range(m):
                node = queue.popleft()
                if node == end:
                    return path
                self.add_neighbors(node, queue, dict, visited)
            path += 1
        return 0

    # use a helper methods.
    def add_neighbors(self, node, queue, dict, visited):
        a = ord('a')
        for i in range(len(node)):
            for j in range(26):
                ne = node[0:i] + chr(a + j) + node[i+1:]
                if ne not in visited and ne in dict:
                    queue.append(ne)
                    visited.add(ne)

if __name__ == '__main__':
    s = Solution()
    s.ladderLength('a', 'c', ['b'])
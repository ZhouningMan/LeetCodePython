from collections import *
import string

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        if start == end:
            return []
        # reverse the bfs
        dict = set(dict)
        dict.add(end)
        dict.add(start)
        # build the distances which is used to prune the dfs
        distances = self.bfs(end, dict)
        ans = []
        # exhaust all paths that satisfy the conditions
        self.dfs(start, end, [start], dict, distances, ans)
        return ans

    # run bfs to build the distances from the end to all dictionary nodes
    # including the start and end. This result will be used to filter
    # the dfs
    def bfs(self, start, dict):
        queue = deque([start])
        # find shortest distance to every dictionary node
        distances = {start: 0}
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                for w in self.getNextWords(word, dict):
                    if w in distances:  # distance also acts as the seen set
                        continue
                    distances[w] = distances[word] + 1
                    queue.append(w)
        return distances

    def dfs(self, curr, end, path, dict, distances, ans):
        if curr == end:
            ans.append(list(path))
            return

        for word in self.getNextWords(curr, dict):
            # Use the distances to prune the search
            if distances[word] > distances[curr] - 1:
                continue
            path.append(word)
            self.dfs(word, end, path, dict, distances, ans)
            path.pop()

    # use generator to generate next element
    def getNextWords(self, curr,  dict):
        for i in range(len(curr)):
            for c in string.ascii_lowercase:
                word = curr[0:i] + c + curr[i+1:]
                if word in dict:
                    yield word

if __name__ == '__main__':
    s = Solution()
    ans = s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
    print(ans)
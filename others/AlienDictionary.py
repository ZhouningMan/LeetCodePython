import collections


class Solution: # mistaken this problem for topological sort
    def alienOrder(self, words) -> str:
        if not words or len(words) == 0:
            return ""
        graph = {}
        self.build_graph(words, graph, 0, 0, len(words) - 1)
        print(graph)
        # visited and the topological sort stack are global for the entire graph
        visited = set()
        stack = collections.deque()
        for k in graph.keys():
            if k in visited:
                continue
            if not self.dfs(graph, set(), visited, stack, k):
                return ""
        return ''.join(reversed(stack))

    # def build_graph(self, words) -> dict:
    #     graph = {}
    #     for word in words:
    #         for i in range(1, len(word)):
    #             prev = word[i - 1]
    #             if word[i] == prev:
    #                 continue
    #             if prev not in graph:
    #                 graph[prev] = set()
    #             graph[prev].add(word[i])
    #         if word[-1] not in graph:
    #             graph[word[-1]] = set()
    #
    #     return graph

    def build_graph(self, words, graph, index, start, end):
        if start > end:
            return
        prev = start
        for i in range(start, end + 1):
            if len(words[i]) <= index:
                self.build_graph(words, graph, index + 1, prev, i - 1)
                prev = i + 1
                continue
            cc = words[i][index]
            pc = words[prev][index]
            if cc not in graph:
                graph[cc] = set()
            if cc != pc:
                graph[pc].add(cc)
                self.build_graph(words, graph, index + 1, prev, i - 1)
                prev = i
        self.build_graph(words, graph, index + 1, prev, end)

    def dfs(self, graph, path, visited, stack, k):
        visited.add(k)
        path.add(k)
        for i in graph[k]:
            if i not in visited:
                if i in path:  # cycle detected
                    return False
                else:
                    self.dfs(graph, path, visited, stack, i)
        stack.append(k)
        path.remove(k)
        return True


if __name__ == '__main__':
    print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))
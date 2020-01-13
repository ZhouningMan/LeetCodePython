# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        TreeNode.__repr__ = lambda node: str(node.val)
        graph = defaultdict(set)
        self.build_graph(root, graph)
        visited = {target}
        queue = deque([target])
        steps = 0
        while queue:
            size = len(queue)
            if steps == K:
                break
            for i in range(size):
                head = queue.popleft()
                for nei in graph[head]:
                    if nei in visited:
                        continue
                    queue.append(nei)
                    visited.add(nei)
            steps += 1
        if steps != K:
            return []
        ans = [node.val for node in queue]
        return ans

    def build_graph(self, node, graph):
        if not node:
            return
        for child in [node.left, node.right]:
            if not child:
                continue
            graph[node].add(child)
            graph[child].add(node)
            self.build_graph(child, graph)
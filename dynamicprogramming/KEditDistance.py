# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26
#         self.word = None
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for c in word:
#             idx = ord(c) - ord('a')
#             if node.children[idx] is None:
#                 node.children[idx] = TrieNode()
#             node = node.children[idx]
#         node.word = word
#
class SolutionMemoryLimitExceeded:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        trie = self.build_trie(words)
        root = trie.root
        dp = {}
        for j in range(0, len(target) + 1):
            dp[(root, j)] = j
        self.dfs(root, dp, target, k)
        result = []
        for (node, j), v in dp.items():
            if node.word is not None and j == len(target) and v <= k:
                result.append(node.word)
        return result

    def build_trie(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie

    def dfs(self, parent, dp, target, k):
        if parent is None:
            return
        for i in range(26):
            child = parent.children[i]
            if not child:
                continue
            self.edit_distance(child, parent, dp, chr(i + ord('a')), target)
            # if dp[(child, len(target))] > k:
            #     continue
            self.dfs(child, dp, target, k)

    def edit_distance(self, child, parent, dp, c, target):
        dp[(child, 0)] = dp[(parent, 0)] + 1
        for j in range(1, len(target) + 1):
            dp[(child, j)] = dp[(parent, j-1)]
            if c != target[j - 1]:
                dp[(child, j)] += 1
            dp[(child, j)] = min(dp[(child, j - 1)] + 1,
                                 dp[(parent, j)] + 1,
                                 dp[(child, j)])

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = word

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        trie = self.build_trie(words)
        root = trie.root
        memo = set()
        dist = [0] * (len(target) + 1)
        for i in range(len(target) + 1):
            dist[i] = i
        self.dfs(root, memo, dist, target, k)
        return list(memo)

    def build_trie(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie

    def dfs(self, parent, memo, dist, target, k):
        if parent is None:
            return
        # find the words, solution found
        if parent.word is not None and dist[-1] <= k:
            memo.add(parent.word)

        for i in range(26):
            child = parent.children[i]
            if not child:
                continue
            # Conventional edit distance
            # dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1,
            # dist is the dp[i-1]
            # we need to produce new dist
            new_dist = self.edit_distance(dist, chr(i + ord('a')), target)
            self.dfs(child, memo, new_dist, target, k)

    def edit_distance(self, dist, c, target):
        new_dist = [0] * len(dist)
        new_dist[0] = dist[0] + 1
        for j in range(1, len(target) + 1):
            # replace: dp[i][j] = dp[i-1][j-1] + 1 | A[i - 1] != B[j-1]
            new_dist[j] = dist[j-1]
            if c != target[j - 1]:
                new_dist[j] += 1
            new_dist[j] = min(dist[j] + 1,  # deletion
                              new_dist[j-1] + 1,  # insertion
                              new_dist[j])
        return new_dist

if __name__ == '__main__':
    s = Solution()
    res = s.kDistance(["abc", "abd", "abcd", "adc"], "ac", 1)
    print(res)
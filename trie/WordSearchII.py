class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Node()
            node = node.children[idx]
        node.word = word

    def find(self, prefix):
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return None
            node = node.children[idx]
        return node


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def wordSearchII(self, board, words):
        if not board or len(board) == 0:
            return []

        trie = self.build_trie(words)
        m = len(board)
        n = len(board[0])
        result = set()
        for r in range(m):
            for c in range(n):
                self.dfs(result, trie, '', board, set(), r, c)
        return sorted(list(result))

    def build_trie(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie

    def dfs(self, result, trie, word, board, visited, r, c):
        visited.add((r, c))
        word += board[r][c]
        node = trie.find(word)
        if not node:
            visited.remove((r, c))
            return
        if node.word is not None:
            result.add(node.word)
        for delta in DIRECTIONS:
            next_r = r + delta[0]
            next_c = c + delta[1]
            if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and (next_r, next_c) not in visited:
                self.dfs(result, trie, word, board, visited, next_r, next_c)
        visited.remove((r, c))

if __name__ == '__main__':
    s = Solution()
    print(s.wordSearchII(["abce","sfes","adee"],["abceseedasfe","abceseeefs"]))
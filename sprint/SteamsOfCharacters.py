from collections import deque


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

    def contains(self, word):
        ri = reversed(word)
        node = self.root
        while node:
            nc = next(ri, None)
            if not nc:
                return False
            node = node.children[ord(nc) - ord('a')]
            if node and node.word:
                return True
        return False


class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        self.limit = 0
        for w in words:
            self.trie.insert(w[::-1])  # reverse the word
            self.limit = max(self.limit, len(w))
        self.buffer = deque()

    def query(self, letter: str) -> bool:
        if len(self.buffer) >= self.limit:
            self.buffer.popleft()
        self.buffer.append(letter)
        return self.trie.contains(self.buffer)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
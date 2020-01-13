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
            idx = self._index(c)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = word

    def _index(self, char):
        return ord(char) - ord('a')

    def search(self, word):
        node = self.get_node(word)
        return node is not None and node.word is not None

    def get_node(self, word):
        node = self.root
        for c in word:
            idx = self._index(c)
            if not node.children[idx]:
                return None
            node = node.children[idx]
        return node

    def startsWith(self, prefix):
        node = self.get_node(prefix)
        return node is not None

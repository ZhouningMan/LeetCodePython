class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self._insert(self.root, word, 0)

    def _insert(self, node, word, i):
        if i == len(word):
            node.word = word
            return
        idx = ord(word[i]) - ord('a')
        if node.children[idx] is None:
            node.children[idx] = TrieNode()
        self._insert(node.children[idx], word, i + 1)

    def search(self, word):
        node = self._find(self.root, word, 0)
        return node is not None and node.word is not None

    def _find(self, node, word, i):
        if node is None:
            return None
        if i == len(word):
            return node
        return self._find(node.children[ord(word[i]) - ord('a')], word, i + 1)


    def startsWith(self, prefix):
        node = self._find(self.root, prefix, 0)
        return node is not None

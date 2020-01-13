class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            idx = self._index(c)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = word

    def search(self, word):
        if not word:
            return False
        return self._search(self.root, word, 0)

    def _search(self, node, word, i):
        if not node:
            return False
        if i == len(word):
            return node.word is not None
        c = word[i]
        if c == '.':
            matched = False
            for child in node.children:
                matched = self._search(child, word, i + 1)
                if matched:
                    return True
            return matched
        else:
            return self._search(node.children[self._index(c)], word, i + 1)


    def _index(self, char):
        return ord(char) - ord('a')
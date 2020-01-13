class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, word):
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.words.add(word)

    def search(self, key):
        node = self.root
        for c in key:
            if c not in node.children:
                return set()
            node = node.children[c]

        return node.words


class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """

    def __init__(self, dict):
        self.trie = Trie()
        for word in dict:
            for i in range(len(word)):
                self.trie.insert(word[i: len(word)], word)

    """
    @param: str: a string
    @return: a list of words
    """

    def search(self, str):
        return sorted(self.trie.search(str))
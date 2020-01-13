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

        # don't forget this step
        node.word = word

    def contains(self, prefix):
        node = self._find(prefix)
        return node is not None

    def _find(self, prefix):
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return None
            node = node.children[idx]
        return node

    def collect(self, prefix):
        node = self._find(prefix)
        result = []
        self._collect(result, node)
        return result

    def _collect(self, result, node):
        if not node:
            return
        if node.word is not None:
            result.append(node.word)
        for child in node.children:
            self._collect(result, child)


class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        result = []
        if not words or len(words) == 0:
            return result
        trie = self.build_trie(words)
        length = len(words[0])
        self.build(result, [], words, 0, length, trie)
        return result

    def build_trie(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie

    def build(self, result, candidate, words, pos, length, trie):
        # no words to complete the word squares, we cannot build a square
        if not words:
            return
        # if reach last step, every word can complete the word square
        if pos == length - 1:
            for w in words:
                result.append(candidate + [w])
            return

        for w in words:
            # append the current word
            candidate.append(w)
            # check if such candidate is valid
            if not self.valid(candidate, trie, length):
                # backtrack
                candidate.pop()
                continue
            # get a list of words with the right prefix
            prefix = self.prefix(candidate, pos + 1)
            self.build(result, candidate, trie.collect(prefix), pos + 1, length, trie)
            # backtrack
            candidate.pop()

    def valid(self, candidate, trie, length):
        if len(candidate) <= 1:
            return True
        size = len(candidate)
        # we want to make sure all the tail prefix exists
        for i in range(size, length):
            if not trie.contains(self.prefix(candidate, i)):
                return False
        return True

    def prefix(self, candidate, i):
        pre = []
        # build the prefix from the string
        for s in candidate:
            pre.append(s[i])
        return pre

if __name__ == '__main__':
    s = Solution()
    print(s.wordSquares(["area","lead","wall","lady","ball"]))
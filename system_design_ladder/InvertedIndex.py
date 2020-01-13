from .Helper import Document

class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        inverted = {}
        for doc in docs:
            words = doc.contents.split()
            for w in words:
                if w not in inverted:
                    inverted[w] = set()
                inverted[w].add(doc.id)
        result = {}
        for k, v in inverted.items():
            result[k] = sorted(list(v))
        return result



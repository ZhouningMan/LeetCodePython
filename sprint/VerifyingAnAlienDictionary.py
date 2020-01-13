class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words:
            return True
        ordial = {k:i for i, k in enumerate(order)}
        prev = words[0]
        for i in range(1, len(words)):
            curr = words[i]
            min_len = min(len(prev), len(curr))
            i =0
            while i < min_len:
                if ordial[curr[i]] < ordial[prev[i]]:
                    return False
                if ordial[curr[i]] > ordial[prev[i]]:
                    break
                i += 1
            # make sure the longer string is after the shorter one.
            if i == min_len and len(curr) < len(prev):
                return False
            prev = curr
        return True
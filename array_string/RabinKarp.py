FACTOR = 31
BASE = 9000001
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if target is None or source is None:
            return -1
        if target == "":
            return 0

        # h(t) = h(t-1) * p + s[t] - p^M * s[t - M] where M = len(target)
        m = len(target)
        pm = 1
        # pre-calculate the power
        for i in range(m):
            pm = (pm * FACTOR) % BASE
        # find the target hash
        target_hash = 0
        for c in target:
            target_hash = (target_hash * FACTOR + ord(c)) % BASE
        source_hash = 0
        for i, c in enumerate(source):
            source_hash = (source_hash * FACTOR + ord(c)) % BASE
            if i < m - 1:
                continue
            if i >= m:
                # We don't necessary to add the BASE because in python that is implied
                # - k % BASE = (BASE - k) % BASE
                source_hash = (source_hash + BASE - pm * ord(source[i - m])) % BASE
            if source_hash == target_hash and source[i-m+1: i+1] == target:
                return i-m+1
        return -1

if __name__ == '__main__':
    s = Solution()
    res = s.strStr("tartarget", "target")
    print(res)
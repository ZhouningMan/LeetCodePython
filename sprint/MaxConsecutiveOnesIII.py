class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = 1 if A[0] == 0 else 0
        length = 0
        j = 0
        for i in range(1, len(A)):
            if A[i] == 0:
                count += 1
            while count > K and j <= i:
                if A[j] == 0:
                    count -= 1
                j += 1
            # A[i: j+1] contains the string
            length = max(length, i + 1 - j)
        return length
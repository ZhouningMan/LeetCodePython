from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        count = 0
        size = len(A)
        left = 0
        right = 0
        min_win = defaultdict(int)
        max_win = defaultdict(int)
        for i in range(0, size - K + 1):
            # find the minimum window that satisfy the condition
            # A[i:left] contains the minimum number of window(left non inclusive)
            while len(min_win) < K and left < size:
                min_win[A[left]] += 1
                left += 1
            # find the maximum window that satisfy the condition
            # A[i:right] contains the maximum number of window(right non inclusive)
            while len(max_win) <= K and right < size:
                if len(max_win) == K and A[right] not in max_win:
                    break
                max_win[A[right]] += 1
                right += 1

            # if the conditon is satisfied
            if len(min_win) == K and len(max_win) == K:
                count += right - left + 1
            min_win[A[i]] -= 1
            max_win[A[i]] -= 1

            # remove key that doesn't exist in the window anymore
            if min_win[A[i]] == 0:
                del min_win[A[i]]
            if max_win[A[i]] == 0:
                del max_win[A[i]]
        return count
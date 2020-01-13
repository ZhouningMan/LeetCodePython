class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        if not times or len(times) == 0:
            return -1
        if n == 0:
            return 0

        start, end = min(times), max(times) * n
        while start <= end:
            mid = start + (end - start) // 2
            books = self.copy_books(times, mid)
            if books < n:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def copy_books(self, times, time):
        count = 0
        for t in times:
            count += time // t
        return count
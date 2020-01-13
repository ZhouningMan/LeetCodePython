class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages or len(pages) == 0:
            return 0
        if k <= 0:
            raise ValueError("...")

        start = max(pages)
        end = sum(pages)
        while start <= end:
            mid = start + (end - start) // 2
            people = self._find_people(pages, mid)
            if people > k:
                # we need more people than we have
                # more time is required
                start = mid + 1
            else:
                end = mid - 1
        return start

    def _find_people(self, pages, time):
        count = 1
        left = time # start with one copier
        for page in pages:
            if left >= page:
                left -= page
            else:
                # use a new copier
                count += 1
                left = time - page
        return count

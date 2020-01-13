#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        start = 1 # this is a one based problem but there is no problem
        end = n
        while start <= end:
            mid = (start + end) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return end + 1 # assuming there is always a bad version.
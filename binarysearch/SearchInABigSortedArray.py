"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index,
        # return 2147483647 if the index is invalid.
"""


class ArrayReader(object):
    def get(self, index):
        pass


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        start = 0
        end = self.find_end_index(reader, target)
        while start + 1 < end:
            mid = (start + end) // 2
            mid_val = reader.get(mid)
            if mid_val < target:
                start = mid + 1
            elif mid_val == target:
                end = mid  # this is the key
            else:
                end = mid - 1
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1

    def find_end_index(self, reader, target):
        i = 1
        while reader.get(i) < target:
            i = i * 2
        return i

    def searchBigSortedArraySimplified(self, reader, target):
        start = 0
        end = self.find_end_index(reader, target)
        while start <= end:
            mid = (start + end) // 2
            mid_val = reader.get(mid)
            if mid_val < target:
                start = mid + 1
            else:
                end = mid - 1
        if reader.get(end + 1) == target:
            return end + 1
        else:
            return -1



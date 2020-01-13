"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""

# class Comparator:
#     def cmp(self, a, b):
#         # aL = a.lower()
#         # bL = b.lower()
#         if a == b:
#             return 0
#         elif a < b:
#             return -1
#         else:
#             return 1

class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        if not nuts or not bolts:
            return
        m = len(nuts)
        n = len(bolts)
        if m != n:
            return
        self.sort(nuts, bolts, compare.cmp, 0, m - 1)

    def sort(self, nuts, bolts, compare, start, end):
        if start >= end:  # nothing to sort
            return
        pivot = nuts[start]
        left, right = self.partition(bolts, start, end, pivot, compare)
        self.partition(nuts, start, end, bolts[left], compare)
        self.sort(nuts, bolts, compare, start, left - 1)
        self.sort(nuts, bolts, compare, right + 1, end)

    def partition(self, values, start, end, pivot, compare):
        if start >= end:
            return start, start
        lt = start
        i = start

        def swap(idx1, idx2):
            values[idx1], values[idx2] = values[idx2], values[idx1]

        while i <= end:
            cmp = compare(values[i], pivot)
            if compare(values[i], pivot) == -1 or compare(pivot, values[i]) == 1:  # smaller than pivot:
                swap(lt, i)
                lt += 1
                i += 1
            elif compare(values[i], pivot) == 1 or compare(pivot, values[i]) == -1:
                # end is only decrement by one when it is greater than
                swap(i, end)
                end -= 1
            else:
                i += 1
        # anything within [lt, end] have the same value as pivot
        # if lt > end, then pivot is  not in the partition
        return lt, end

if __name__ == '__main__':
    # s = Solution()
    # nuts = [1, 3, 5,2]
    # bolts = [2, 5,3, 1]
    # s.sortNutsAndBolts(nuts, bolts, Comparator())
    # print(nuts)
    # print(bolts)



    s = Solution()
    values = [12, 2, 3, 4, 1,7,2,4,4,6]
    def comp(x, y):
        if x == y:
            return 0
        elif x > y:
            return 1
        else:
            return -1
    print(s.partition(values, 0, len(values) - 1, 5, comp))
    print(values)
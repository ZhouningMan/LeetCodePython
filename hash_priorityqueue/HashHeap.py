# class HashHeap:
#     def __init__(self):
#         self.heap = [None] # 1-based
#         self.idx_map = {}
#
#     def empty(self):
#         return len(self.heap) == 1
#
#     def top(self):
#         return self.heap[1]
#
#     def push(self, item):
#         self.heap += [item]
#         idx = len(self.heap) - 1
#         self.idx_map[item] = idx
#         self._up(idx)
#
#     def pop(self):
#         val = self.heap[1]
#         self.remove(val)
#
#     def remove(self, val):
#         if val not in self.idx_map:
#             return
#         idx = self.idx_map[val]
#         n = len(self.heap) - 1
#         self._swap(idx, n)
#         self.heap.pop()  # remove last element
#         del self.idx_map[val]
#         if idx < n:
#             self._up(idx)
#             self._down(idx)
#
#     def _up(self, i):
#         while i > 1 and self._greater(i//2, i):
#             self._swap(i, i//2)
#             i = i//2
#
#     def _down(self, i):
#         n = len(self.heap) - 1
#         while 2*i <= n:
#             j = 2*i
#             # find the better child
#             if j < n and self._greater(j, j+1):
#                 j += 1
#             if not self._greater(i, j):
#                 break
#             self._swap(i, j)
#             i = j
#
#     def _greater(self, i, j):
#         return self.heap[i] > self.heap[j]
#
#     def _swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#         self.idx_map[self.heap[i]] = i
#         self.idx_map[self.heap[j]] = j


class HashHeap:

    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def push(self, item):
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)

    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item

    def top(self):
        return self.heap[0]

    def remove(self, item):
        if item not in self.hash:
            return

        index = self.hash[item]
        self._swap(index, self.size - 1)

        del self.hash[item]
        self.heap.pop()

        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = index // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 < self.size:
            smallest = index
            left = index * 2
            right = index * 2 + 1

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i


if __name__ == '__main__':
    nums = [1, 1,  1, 1]
    hash_heap = HashHeap()
    for num in nums:
        hash_heap.push(num)

    for num in nums:
        print(hash_heap.top())
        hash_heap.remove(num)



def print_heap(heap):
    increasing = []
    while not heap.empty():
        increasing.append(heap.pop())
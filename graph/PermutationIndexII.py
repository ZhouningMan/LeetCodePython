from collections import defaultdict


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        index = 1
        size = len(A)
        fact = self.factorial(size)
        repeated = self.repeated_map(A)
        for i in range(size):
            # count how many of them are smaller than the current value
            count = self.smaller(A, i)
            fact //= size - i
            index += count * fact // repeated[i + 1]
        return index

    def factorial_map(self, A):
        num_map = defaultdict(int)
        depulicate = 1
        fact = 1
        for i in range(len(A), 0, -1):
            fact

        return repeated



    def repeated_map(self, A):
        repeated = {len(A): 1}
        num_map = defaultdict(int)
        val = 1
        for i in range(len(A) - 1, -1, -1):
            num_map[A[i]] += 1
            val *= num_map[A[i]]
            repeated[i] = val
        return repeated


    # smaller from ith, because, we have fixed
    # prefix
    def smaller(self, A, i):
        val = A[i]
        count = 0
        for i in range(i, len(A)):
            if A[i] < val:
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    s.permutationIndexII([3,2,2,1,1])

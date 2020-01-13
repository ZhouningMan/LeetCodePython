class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        index = 1
        size = len(A)
        fact = self.factorial(size)
        for i in range(size):
            # count how many of them are smaller than the current value
            count = self.smaller(A, i)
            fact //= size - i
            index += count * fact
        return index

    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    # smaller from ith, because, we have fixed
    # prefix
    def smaller(self, A, i):
        val = A[i]
        count = 0
        for i in range(i, len(A)):
            if A[i] < val:
                count += 1
        return count



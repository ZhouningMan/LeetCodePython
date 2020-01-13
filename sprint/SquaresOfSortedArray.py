class Solution:
    def sortedSquares(self, A):
        size = len(A)
        squares = [0] * size
        for i in range(size):
            squares[i] = A[i] * A[i]
        copy = [0] * size
        begin = 0
        end = size - 1
        i = size - 1
        while begin <= end:
            if squares[begin] > squares[end]:
                copy[i] = squares[begin]
                begin += 1
            else:
                copy[i] = squares[end]
                end -= 1
            i -= 1
        return copy

if __name__ == '__main__':
    s = Solution()
    ans = s.sortedSquares([-3,-3,-2,1])
    print(ans)
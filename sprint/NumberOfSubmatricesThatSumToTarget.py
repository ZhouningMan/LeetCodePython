from collections import defaultdict
class Solution:
    # improve brute force algorithm
    def numSubmatrixSumTargetImprovedBruteForce(self, matrix, target: int) -> int:
        # TODO validation
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        for br in range(rows):
            colSum = [0] * cols
            for er in range(br, rows):
                for c in range(cols):
                    colSum[c] += matrix[er][c]
                for bc in range(cols):
                    s = 0
                    for ec in range(bc, cols):
                        s += colSum[ec]
                        if s == target:
                            ans += 1
        return ans

    # optimized version
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        for br in range(rows):
            colSum = [0] * cols
            for er in range(br, rows):
                preSumMap = defaultdict(int)
                preSum = 0
                preSumMap[0] = 1
                for c in range(cols):
                    colSum[c] += matrix[er][c]
                    preSum += colSum[c]
                    ans += preSumMap[preSum - target]
                    preSumMap[preSum] += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    ans = s.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0)
    print(ans)

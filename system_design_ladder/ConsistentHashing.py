class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        results = [[0, 359, 1]]
        for i in range(1, n): # incrementally build the matrix
            index = 0
            # locate the range to be split
            for j in range(i):
                if results[j][1] - results[j][0] > results[index][1] - results[index][0]:
                    index = j
            x, y = results[index][0], results[index][1]
            results[index][1] = (x + y) // 2
            results.append([(x + y) // 2 + 1, y, i + 1])

        return results

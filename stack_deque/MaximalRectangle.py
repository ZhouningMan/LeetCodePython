class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        height = [0] * n
        area = 0
        for i in range(m):
            for j in range(n):
                height[j] = 0 if matrix[i][j] == 0 else 1 + height[j]
            area = max(area, self.largestRectangleArea(height))
        return area

    def largestRectangleArea(self, height):
        if not height or len(height) == 0:
            return 0
        stack = [-1]  # this is a nice trick that ease the implementation a lot.
        area = -1
        for i, h in enumerate(height):
            # a little bit like double pointer solution
            # keep find removing elements that doesn't satisfy our condition
            # and remove them, while removing them, compute the local optimum
            while len(stack) > 1 and h <= height[stack[-1]]:
                left = stack.pop()
                # compute the area using the height of left rectangle.
                area = max(area, (i - stack[-1] - 1) * height[left])
            stack.append(i)

        # once we have build the monotunous stack
        # rectangle started at every index can reach the right most position
        right = len(height)
        while len(stack) > 1:
            idx = stack.pop()
            area = max(area, (right - stack[-1] - 1) * height[idx])
        return area

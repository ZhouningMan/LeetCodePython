class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
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



class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, r, c):
        rows = len(image)
        cols = len(image[0])
        left = self.find_left(image, 0, c)
        right = self.find_right(image, c, cols - 1)
        top = self.find_top(image, 0, r)
        bottom = self.find_bottom(image, r, rows - 1)
        return (bottom - top + 1) * (right - left + 1)

    def find_left(self, image, start, end):
        while start <= end:
            mid = (start + end) // 2
            if self.empty_col(image, mid):
                start = mid + 1
            else:
                end = mid - 1
        return start

    def find_right(self, image, start, end):
        while start <= end:
            mid = (start + end) // 2
            if self.empty_col(image, mid):
                end = mid - 1
            else:
                start = mid + 1
        return end

    def empty_col(self, image, c):
        for row in image:
            if row[c] == "1":
                return False
        return True

    def find_top(self, image, start, end):
        while start <= end:
            mid = (start + end) // 2
            if self.empty_row(image, mid):
                start = mid + 1
            else:
                end = mid - 1
        return start

    def find_bottom(self, image, start, end):
        while start <= end:
            mid = (start + end) // 2
            if self.empty_row(image, mid):
                end = mid - 1
            else:
                start = mid + 1
        return end

    def empty_row(self, image, r):
        for c in range(len(image[0])):
            if image[r][c] == "1":
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    input = ["11001100000",
"11101100000",
"11111111010",
"11111111111",
"11111111111",
"11111110111",
"11111111111",
"11111111111",
"11111111111",
"11111111111",
"11111000001",
"11111111011",
"11111110000",
"11110000000",
"11110000000",
"11111000000",
"11000000000",
"11000000000",
"11111000000",
"11111100000",
"11111000000",
"11111000000",
"01110000000"]
    res = s.minArea( input, 0, 1)
    print(res)
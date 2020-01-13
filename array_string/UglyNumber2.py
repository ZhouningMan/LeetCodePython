class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n <= 0:
            raise ValueError("....")
        previou_u = [1]
        a, b, c = 0, 0, 0
        for i in range(1, n):
            next_u = min(2 * previou_u[a], 3 * previou_u[b], 5 * previou_u[c])
            print((a, b, c, next_u))
            if next_u == 2 * previou_u[a]:
                a += 1
            if next_u == 3 * previou_u[b]:
                b += 1
            if next_u == 5 * previou_u[c]:
                c += 1
            previou_u.append(next_u)
        return previou_u[-1]

if __name__ == '__main__':
    s = Solution()
    s.nthUglyNumber(41)

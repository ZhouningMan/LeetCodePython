class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_away = 2
        two_away = 1
        for i in range(3, n + 1):
            ways = one_away + two_away
            # i had it wrong, now both one_away and two_away
            # one_away = ways
            # two_away = one_away
            two_away = one_away
            one_away = ways
        return one_away

if __name__ == '__main__':
    s = Solution()
    input = [1, 2, 3, 4, 5, 6, 7]
    for i in input:
        print(s.climbStairs(i))

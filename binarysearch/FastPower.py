class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        ans = 1
        p = a
        # modulo arithmatic
        while n > 0:
            if n % 2 == 1: # whether the first bit is 1 or not
                ans = (ans * p) % b
            p = (p * p) % b
            n //= 2
        # don't forget to do a modulo for ans
        return ans % b

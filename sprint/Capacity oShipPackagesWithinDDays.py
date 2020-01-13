class Solution:
    def shipWithinDays(self, weights, D):
        if not weights or D <= 0:
            raise ValueError("Invalid input...")

        low = max(weights)
        hi = sum(weights)
        while low <= hi:
            mid = low + (hi - low) // 2
            days = self.days(weights, mid)
            if days <= D:
                # can i do it with less capacity
                hi = mid - 1
            else:
                low = mid + 1
        # this is the minimum capacity we can do it
        return low

    def days(self, weights, capacity):
        count = 0
        curr = 0
        for w in weights:
            if curr + w <= capacity:
                curr += w
            else:
                count += 1
                curr = w
        count += 1 # last ship
        return count

if __name__ == '__main__':
    s = Solution()
    ans = s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
    print(ans)
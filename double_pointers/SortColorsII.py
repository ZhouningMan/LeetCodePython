class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if not colors:
            return
        self.partitionTwoWay(colors, 0, len(colors) - 1, 1, k)

    def partition(self, colors, start, end, ks, ke):
        if start >= end:
            return
        if ks >= ke:
            return
        # partition
        km = (ks + ke) // 2
        i = start
        gt = end
        lt = start
        # three way partitions
        while i <= gt:
            # for all colors greater than the middle color, put them to the right
            if colors[i] > km:
                colors[i], colors[gt] = colors[gt], colors[i]
                gt -= 1
            elif colors[i] == km:
                i += 1
            else:
                colors[i], colors[lt] = colors[lt], colors[i]
                i += 1
                lt += 1
        # after the partition
        # colors [lt, gt] are equals to km
        self.partition(colors, start, lt - 1, ks, km - 1)
        self.partition(colors, gt + 1, end, km + 1, ke)

    def partitionTwoWay(self, colors, start, end, ks, ke):
        if start >= end:
            return
        if ks >= ke:
            return
        # partition
        km = (ks + ke) // 2
        i = start
        j = end
        while i <= j:
            # for all colors greater than the middle color, put them to the right
            if colors[i] > km:
                colors[i], colors[j] = colors[j], colors[i]
                j -= 1
            else:
                i += 1
        # after the partition
        # colors: [0, j] are smaller than km
        # colors: [1, end] are no smaller than km
        self.partitionTwoWay(colors, start, j, ks, km)  # km is left leaning
        self.partitionTwoWay(colors, i, end, km + 1, ke)


if __name__ == '__main__':
    s = Solution()
    A = [2,1,1,2,2]
    s.sortColors2(A, 2)
    print(A)
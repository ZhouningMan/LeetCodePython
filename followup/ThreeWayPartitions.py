def partition(values, start, end, pivot, compare):
    if start >= end:
        return start, start
    lt = start
    i = start

    def swap(idx1, idx2):
        values[idx1], values[idx2] = values[idx2], values[idx1]

    while i <= end:
        cmp = compare(values[i], pivot)
        # always swap lt with i and increment both
        if cmp == -1:  # smaller than pivot:
            swap(lt, i)
            lt += 1
            i += 1
        elif cmp == 1:
            # end is only decremented by one when it is greater than
            swap(i, end)
            end -= 1
        else:
            i += 1
    # anything within [lt, end] have the same value as pivot
    # if lt > end, then pivot is  not in the partition
    return lt, end
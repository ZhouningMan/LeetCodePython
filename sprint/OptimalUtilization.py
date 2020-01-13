MAX_INT = 2**31 - 1
def optimalUtilization(a, b, target):
    def sort_key(v):
        return v[1], v[0]
    a.sort(key=sort_key)
    b.sort(key=sort_key)

    ai = 0
    bi = len(b) - 1
    ans = []
    diff = MAX_INT
    while ai < len(a) and bi >= 0:
        a_val = a[ai][1]
        b_val = b[bi][1]
        if a_val + b_val > target:
            bi -= 1
            continue
        new_diff = target - a_val - b_val
        i = a[ai][0]
        j = b[bi][0]
        if new_diff < diff:
            # create a new list
            # don't forget to assign new_diff to diff
            diff = new_diff
            ans = [[i, j]]
        elif new_diff == diff:
            ans.append([i, j])
        ai += 1
    return ans

class TestCase:
    def __init__(self, a, b, target):
        self.a = a
        self.b = b
        self.target = target

    def __repr__(self):
        return f"a = {self.a}; b = {self.b}, target = {self.target}"

if __name__ == '__main__':
    testcases = [
        TestCase([[1, 2], [2, 4], [3, 6]], [[1, 2]], 7),
        TestCase([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10),
        TestCase([[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20),
        TestCase([[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20)
    ]

    results = [
        [[2, 1]],
        [[2, 4], [3, 2]],
        [[3, 1]],
        [[1, 3], [3, 2]]
    ]

    for tc, re in zip(testcases, results):
        result = optimalUtilization(tc.a, tc.b, tc.target)
        if re == result:
            print(str(tc) + "  OK")
        else:
            print(str(tc) + " FAILED")
            print("Actual: " + str(result))
            print("Expected: " + str(re))
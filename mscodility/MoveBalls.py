# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

MAX_INT = 2 ** 31 - 1
LIMIT = 10 ** 9
RED = 'R'

def solution(S):
    red_indices = get_red_indices(S)
    red_count = len(red_indices)
    swaps = MAX_INT
    # Brute force algorithm which wil take
    # O(W * R) runtime complexity and O(R) space complexity
    # where W is the total number of white balls and R is the number of red balls
    # in the worse case where W is close to R, the complexity is about N^2

    # The algorithm is basically pick the first position of Red balls at every possible
    # location, and count the number of swaps required to have that configuration
    # it is correct because the result must be one of the configuration
    # but unfortunately it is not efficient, and I wasn't able to come up with
    # an efficient algorithm within the time window
    for i in range(len(S) - red_count + 1): # pick the start location of first red ball
        j = i
        tmp = 0
        # count the number of swaps required to reach the given configuration
        for red_index in red_indices:
            tmp += abs(red_index - j)
            j += 1
        # optimize the solution
        swaps = min(swaps, tmp)
    return swaps if swaps < LIMIT else -1

def get_red_indices(S):
    indices = []
    for i in range(len(S)):
        if S[i] == RED:
            indices.append(i)
    return indices

if __name__ == '__main__':
    #S = "WWWRWWWRWR"
    S = "WWRWRR"
    print(solution(S))

# def count(S):
#     count = 0
#     for b in S:
#         if b == 'R':
#             count += 1
#     return count


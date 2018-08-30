"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
"""
def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    sums = []

    def find_sums(i, arr):
        if len(arr) == k:
            if sum(arr) == n and arr not in sums:
                sums.append(arr)
        else:
            for j in range(i, 10):
                find_sums(j+1, arr.copy() + [j])

    for i in range(1,10): find_sums(i, [])

    return sums

print(combinationSum3(3,7))

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    out, p = [], 1

    for i in nums: p *= i

    for num in nums: 
        if num == 0: out.append(p)
        else: out.append(int(p * num**-1))

    return out

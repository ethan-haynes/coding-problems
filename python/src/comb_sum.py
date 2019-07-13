def combsum(nums, target):
    n = len(nums)
    sums = []
    if n == 0:
        return sums

    for i in range(n):
        num = nums[i]
        remainder = nums[i+1:]
        
        if num == target:
            sums.append([num])
        
        for sub_sum in combsum(remainder, target - num):
            sums.append([num] + sub_sum)
    
    return sums
        
print(combsum([1,2,3,4,5,6,7], 19))
print(combsum([1,2,3,4,5,6,7], 21))
print(combsum([1,2,-1,4,5,6,7], 21))

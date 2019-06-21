def findTriplet(nums):
    N = len(nums)
    squars = set()
    
    for i in range(N):
        for j in range(i, N):
            square = (nums[i]**2 + nums[j]**2)
            if nums[i]**2 in squars:
                return True
            else:
                squars.add(square)

    return False


print(findTriplet([3,2,4,6,5]))

def findTripletWithZeroSum(nums):
    N = len(nums)
    sums = set()

    for i in range(N):
        for j in range(i, N):
            the_sum = nums[i] + nums[j]
            if -(nums[j]) in sums:
                return True
            else:
                sums.add(the_sum)
    return False

print(findTripletWithZeroSum([1,2,3,4,5]))
print(findTripletWithZeroSum([1,0,-1,2,3]))

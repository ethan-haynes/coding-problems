def find_single1(nums):
    s1, s2, single = set(), set(), None
    for i in nums:
        if i not in s1 and i not in s2: s1.add(i)
        else: s2.add(i)
    
    for i in s1:
        if i not in s2:
            single = i
            break
    return single

def find_single2(nums):
    s = set(nums)
    multiple = (len(nums) - 1) / (len(s) - 1)
    return int((sum(s) * multiple - sum(nums))/ (multiple - 1))


arr = [1,2,2,2,3,3,3,4,4,4,5,5,5]

print(find_single1(arr))
print(find_single2(arr))

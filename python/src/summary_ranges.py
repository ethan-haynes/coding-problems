'''
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
'''
def summary_ranges(nums):
    if len(nums) == 0: return nums
    elif len(nums) == 1: return [str(nums[0])]
    out = []
    r, smmry = None, ''
    
    def handle_num():
        if str(r-1) == smmry: out.append(smmry)
        else:
            out.append(smmry + '->{num}'.format(num=str(r-1)))

    for i, v in enumerate(nums):
        if r == None: r, smmry = v + 1, str(v)
        else: 
            if r == v: r += 1
            else:
                handle_num()
                r, smmry = v + 1, str(v)
        
        if i == len(nums) - 1: handle_num()
    return out

print(summary_ranges([0,1,2,4,5,7]))

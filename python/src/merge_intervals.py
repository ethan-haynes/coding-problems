# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + '-' + str(self.end) + ']'

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        prev, offset = None, 0
        for i,ivls in enumerate(intervals):
            if prev:
                if ivls.start <= prev:
                    prev, new_ivls = ivls.end, Interval(intervals[i-1-offset].start, ivls.end)
                    intervals = intervals[:i-1-offset] + [new_ivls] + intervals[i+1-offset:]
                    offset += 1
                else: prev = ivls.end
            else: prev = ivls.end

        return intervals

s = Solution()
for i in s.merge([Interval(1,4),Interval(4,5),Interval(6,10),Interval(9,12)]):
    print(i)

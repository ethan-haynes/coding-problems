import math
class Solution:
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if math.copysign(1,x) == -1:
            return False
        temp = x
        length = math.ceil(math.log10(temp+1) or 1)
        place = 10**(length-1)
        num = 0

        for _ in range(0, length):
            num += temp%10 * place
            temp = math.floor(temp/10)
            place = math.floor(place/10)

        return int(num) == x

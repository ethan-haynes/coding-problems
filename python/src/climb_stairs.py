def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    memo = {}
    def climb(n):
        if n not in memo:
            out = 1
            if n:
                if 2 <= n:
                    out = self.climbStairs(n-1) + self.climbStairs(n-2)
                else:
                    out = self.climbStairs(n-1)
            memo[n] = out
        return memo[n]
    return climb(n)

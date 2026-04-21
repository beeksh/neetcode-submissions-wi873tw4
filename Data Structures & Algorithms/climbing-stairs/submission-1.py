class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1, 2:2}
        def x(n):
            if n in d:
                return d[n]
            else:
                d[n]=x(n-1)+x(n-2)
                return d[n]
        
        return x(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         d = {1:1, 2:2}
#         def x(n):
#             if n in d:
#                 return d[n]
#             else:
#                 d[n]=x(n-1)+x(n-2)
#                 return d[n]
        
#         return x(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        t = [1,2]
        for i in range(2,n):
            t.append(t[i-1]+t[i-2])
        return t[-1]
    
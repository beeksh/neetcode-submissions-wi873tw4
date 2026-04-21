# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         d = {}
#         def x(n):
#             if n>=len(cost):
#                 return 0
#             if n in d:
#                 return d[n]
#             else:
#                 d[n] = cost[n]+min(x(n+1), x(n+2))
#             return d[n]
#         return min(x(0),x(1))

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         d = [0]*(n+2)
#         for i in range(n-1,-1,-1):
#             d[i] = cost[i]+min(d[i+1], d[i+2])
#         return min(d[i], d[i+1])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        for n in range(len(cost)-1, -1, -1):
            curr = cost[n]+min(prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return min(prev1, prev2)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        def x(n):
            if n>=len(cost):
                return 0
            if n in d:
                return d[n]
            else:
                d[n] = cost[n]+min(x(n+1), x(n+2))
            return d[n]
        return min(x(0),x(1))
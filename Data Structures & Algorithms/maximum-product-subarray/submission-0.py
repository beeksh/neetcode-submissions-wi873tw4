class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Smin, Smax, res = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            Tmax = max(num, Smax*num, Smin*num)
            Tmin = min(num, Smax*num, Smin*num)

            Smax = Tmax
            Smin = Tmin

            res = max(res, Smax)
            
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = -float("inf")
        cur = 0
        
        for num in nums:
            temp = cur+num
            if temp>out:
                out=temp
            if temp>0:
                cur = temp
            else:
                cur = 0
        
        return out
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        mc = 0
        for num in nums:
            if num-1 in nums:
                continue
            else: 
                count = 1
                n = num
                while n+1 in x:
                    count +=1
                    n+=1
            if count>mc: mc = count
        return mc
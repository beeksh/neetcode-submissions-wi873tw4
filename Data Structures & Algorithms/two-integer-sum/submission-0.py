class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        a[nums[0]]=0
        for i in range(1,len(nums)):
            if target-nums[i] in a:
                return [a[target-nums[i]], i]
            else:
                a[nums[i]]=i
            
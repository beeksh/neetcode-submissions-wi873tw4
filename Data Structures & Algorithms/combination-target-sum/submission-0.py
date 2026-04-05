class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def b(i, tot, curr):
            if tot == target:
                res.append(curr[:])
                return
            
            if tot>target:
                return
            
            for x in range(i, len(nums)):
                curr.append(nums[x])
                b(x, tot+nums[x], curr)
                curr.pop()
        b(0, 0, [])
        return res

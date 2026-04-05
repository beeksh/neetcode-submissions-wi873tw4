class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def d(curr):
            
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num in curr:
                    continue
                
                curr.append(num)
                d(curr)
                curr.pop()
            
        d([])
        return res
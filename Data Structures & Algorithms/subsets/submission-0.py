class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def b(i, curr):
            if i == len(nums):
                result.append(curr[:])
                return 
            b(i+1, curr)

            curr.append(nums[i])
            b(i+1, curr)
            curr.pop()

        b(0, [])

        return result
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        out = nums[0]

        while l<=r:
            m = (l+r)//2

            if nums[l]<=nums[r]:
                out = min(out, nums[l])
                break
            if nums[l]<=nums[m]:
                l=m+1
            else:
                out = min(out, nums[m])
                r=m-1
        return out
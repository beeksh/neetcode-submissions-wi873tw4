class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            x = l + (r - l) // 2

            if nums[x] == target:
                return x
            elif nums[x] < target:
                l = x + 1
            else:
                r = x - 1

        return -1
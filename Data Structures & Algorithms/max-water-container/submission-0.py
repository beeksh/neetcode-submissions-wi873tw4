class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        ma = 0
        for i in range(len(heights)):
            h = heights[l] if heights[l]<heights[r] else heights[r]
            a = (r-l)*h
            if a > ma: ma = a
            if heights[l]<heights[r]: l+=1
            else: r-=1
        return ma
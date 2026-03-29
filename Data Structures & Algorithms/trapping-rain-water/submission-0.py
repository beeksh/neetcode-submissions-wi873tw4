class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0,len(height)-1
        ml, mr = height[l], height[r]
        t = 0
        while l!=r:
            if ml<mr:
                if min(ml, mr) - height[l]>0:
                    t+= min(ml, mr) - height[l]
                l+=1
                ml = max(ml, height[l])
            else:
                if min(ml, mr) - height[r]>0:
                    t+= min(ml, mr) - height[r]
                r-=1
                mr = max(mr, height[r])
        return t

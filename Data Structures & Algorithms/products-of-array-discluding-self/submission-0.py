class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prod = 1
        zc = 0
        for num in nums:
            if num!=0:
                prod*=num
            else:
                zc+=1
        if zc == 0:
            for num in nums:
                out.append(int(prod/num))
        elif zc == 1:
            for num in nums:
                if num == 0:
                    out.append(prod)
                else:
                    out.append(0)
        else:
            for num in nums:
                out.append(0)
        return out
        

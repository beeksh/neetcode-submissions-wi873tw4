class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def exp(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            x1 = exp(i,i)
            x2 = exp(i,i+1)
            res = max(res,x1,x2,key=len)
        
        return res
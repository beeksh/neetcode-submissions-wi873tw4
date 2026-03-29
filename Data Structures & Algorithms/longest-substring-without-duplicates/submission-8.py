class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        unique = set()
        mlen = 0
        if len(s)==0: return 0
        while r!= len(s):
            if s[r] not in unique:
                unique.add(s[r])
                r+=1
                mlen = max(mlen, r-l)
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l+=1
        return mlen

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l,r = 0,0
        maxq = 0
        for i in range(len(s)):
            
            freq[s[r]] = freq.get(s[r], 0) +1
            maxq = max(freq[s[r]],maxq)
            while (r-l+1) - maxq > k:
                freq[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
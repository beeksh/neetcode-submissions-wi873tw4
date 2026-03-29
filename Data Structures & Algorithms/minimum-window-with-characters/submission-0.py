class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""
        
        
        t1 = {}
        for x in t: t1[x] = t1.get(x,0)+1
        have, need = 0, len(t1)

        t2 = {}
        l = 0
        mins = ""
        minl = float("infinity")
        for r in range(len(s)):
            t2[s[r]] = t2.get(s[r], 0) + 1
            
            if s[r] in t1 and t2[s[r]]==t1[s[r]]:
                have+=1
            while have == need:
                if (r-l+1)<minl:
                    minl = (r-l+1)
                    mins = s[l:r+1]
                t2[s[l]]-=1
                if s[l] in t1 and t2[s[l]] < t1[s[l]]:
                    have -=1
                l +=1

        return mins if minl!= float("infinity") else ""
                
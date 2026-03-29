class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = {}, {}

        if len(s1)>len(s2):
            return False

        for s in s1:
            l1[s] = l1.get(s, 0) + 1
        for i in range(len(s1)):
            l2[s2[i]] = l2.get(s2[i], 0) + 1

        l,r = 0, len(s1)

        if l1==l2:
            return True
        while r!=len(s2):
            if l2[s2[l]]==1:
                l2.pop(s2[l])
            else: l2[s2[l]] = l2.get(s2[l]) - 1
            l+=1
            l2[s2[r]] = l2.get(s2[r], 0) + 1
            r+=1
   
            if l1==l2:
                return True
        return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        st = s.lower()
        while l<r:
            if not st[l].isalnum():
                l+=1
                continue
            if not st[r].isalnum():
                r-=1 
                continue
            if st[r]!=st[l]:
                return False
            r-=1
            l+=1
        return True
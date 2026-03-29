class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: return False
        
        d = {'(':')', '{':'}', '[':']'}
        op = ['(','{','[']
        q = collections.deque()
        for r in s:
            if r in op:
                q.append(r)
                continue
            if r not in op and not q: return False
            if r not in op and q:
                if d[q[-1]]==r: 
                    q.pop()
                else: return False
        if q: return False
        return True
        
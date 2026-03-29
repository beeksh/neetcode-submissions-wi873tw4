class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = {} #{1:1, 2:2, 3:3}
        u = [] #[1,2,3]
        for num in nums:
            if num not in t:
                u.append(num)
            t[num]=t.get(num,0)+1
        # return u
        out = []
        for i in range(k):
            h = 0
            m = 0
            for j in range(len(u)):
                if u[j]!=-1001:
                    if t[u[j]]>m:
                        m=t[u[j]]
                        h = j
            out.append(u[h])
            u[h]=-1001
        return out
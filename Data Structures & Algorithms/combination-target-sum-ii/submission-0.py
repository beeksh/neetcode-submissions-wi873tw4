class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def b(i, tot, curr):
            if tot==target:
                res.append(curr[:])
                return 

            if tot>target:
                return
            
            for x in range(i, len(candidates)):
                if x>i and candidates[x]==candidates[x-1]:
                    continue
                curr.append(candidates[x])
                b(x+1, tot+candidates[x], curr)
                curr.pop()
        
        b(0,0,[])

        return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back(op, cl, curr):
            if len(curr)==2*n:
                res.append(curr[:])
                return 
            if op<n:
                back(op+1, cl, curr+"(")
            if cl<op:
                back(op, cl+1, curr+")")
        back(0,0, "")
        return res
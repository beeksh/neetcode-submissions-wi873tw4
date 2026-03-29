class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        en+=str(len(strs))+"#"
        for st in strs:
            l = len(st)
            en+=str(l)+"#"+st
        return en

    def decode(self, s: str) -> List[str]:#2#5#Hello5#World
        l = ""
        pt = 0
        while s[pt]!="#":
            l+=s[pt]
            pt+=1
        tot = int(l)
        pt+=1
        # return tot
        res = []
        for i in range(tot):
            l = ""
            while s[pt]!="#":
                l+=s[pt]
                pt+=1
            strlen = int(l)
            res.append(s[pt+1:pt+strlen+1])
            pt = pt+strlen+1
        return res







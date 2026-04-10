class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":return []
        hm = {"2":["a","b","c"], "3":["d","e","f"], 
            "4":["g","h", "i"], "5":["j","k","l"],
            "6":["m","n","o"], "7":["p","q","r","s"],
            "8":["t","u", "v"], "9":["w", "x", "y", "z"]
        }

        res = []
    
        def back(i, curr):
            if i==len(digits):
                res.append(curr[:])
                return

            for j in range(len(hm[digits[i]])):
                temp = curr[:]
                curr += hm[digits[i]][j]
                back(i+1, curr)
                curr = temp
        
        back(0,"")

        return res

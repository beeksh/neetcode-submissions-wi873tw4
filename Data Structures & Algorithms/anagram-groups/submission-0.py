class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        for st in strs:
            temp = {}
            for char in st:
                temp[char] = temp.get(char, 0) + 1
            x.append(temp)
        stat = {}
        for i in range(len(strs)):
            stat[i]=0
        out = []
        for i in range(len(strs)):
            if stat[i]==1:
                continue
            else:
                stat[i]=1
                temp = []
                temp.append(strs[i])
                for j in range(i+1, len(strs)):
                    if stat[j]==1:
                        continue
                    if x[i]==x[j]:
                        stat[j]=1
                        temp.append(strs[j])
                out.append(temp)
        return out
                                                
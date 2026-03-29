class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        st = [len(temperatures)-1]

        for i in range(len(temperatures)-1, -1, -1):
            
            while st and temperatures[i]>=temperatures[st[-1]]:
                st.pop()
            if st and temperatures[i]<temperatures[st[-1]]:
                out.append(st[-1]-i)
                st.append(i)
            else:
                out.append(0)
                st.append(i)
            print(i, st, out)
        return out[::-1]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ['+', '-', '*', '/']
        for t in tokens:
            print(st)
            if t not in op:
                st.append(int(t))
                continue
            if t in op:
                a = st.pop()
                b = st.pop()
                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(b-a)
                elif t == '*':
                    st.append(a*b)
                else:
                    st.append(int(b/a))
        return st[-1]
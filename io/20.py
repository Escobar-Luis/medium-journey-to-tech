class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        h={')':'(',']':'[','}':'{'}
        for v in s:
            if v in h:
                if st and h[v]==st[-1]:
                    st.pop()
                else:
                    return False
            else:
                st.append(v)
        print(st)
        return True if not st else False
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(s):
            stk = []
            for ch in s:
                if ch=="#":
                    if stk: stk.pop()
                else:
                    stk.append(ch)
            return stk
        return remove(s)==remove(t)
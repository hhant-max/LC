class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def removeback(string):
            res = []
            for i in string:
                if i != '#':
                    res.append(i)
                else:
                    # 去掉最后一个
                    if res: res.pop()
            return res
        
        if removeback(s) == removeback(t): 
            return True
        else:
            return False
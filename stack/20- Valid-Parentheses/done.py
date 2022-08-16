class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")":"(", "}":"{","]":"["}
        
#         for i in s:
#             stack.append(i)
        #并没有直接来遍历 二十直接筛选 有一个开头的话 就直接走下去 如果没有开头就不必走了肯定不符合 
        # 关键点是吧遍历转化成了一个条件的判断
        
        for c in s:
            if c in parentheses:
                # 成功有开头
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
                
        return True if not stack else False
        
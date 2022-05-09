class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2 : return x

        left, right, res = 0, x,-1
        while left < right:
            m = left + (right-left)//2
            if m*m ==x:
                return m
            elif x < m*m:
                right = m
            else:
                left = m +1
                res = m
        return res
                

        

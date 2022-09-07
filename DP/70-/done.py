class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 1: return n
        one,two = 2,1
        
        for _ in range(n-2):
            one, two = one + two,one
        return one 
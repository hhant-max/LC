class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        q = int(sqrt(c))
        for a in range(q+1):
            b = sqrt(c-a**2)
            if b == int(b): return True
        return False
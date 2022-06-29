class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.addSumSquare(n)
            if n == 1: return True
        
        return False
            
    def addSumSquare(self, n:int) -> int:
        square = 0 
        for digit in str(n):
            square += int(digit) **2
        return square
        
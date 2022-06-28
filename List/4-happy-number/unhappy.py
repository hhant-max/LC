class Solution:
    def isHappy(self, n: int) -> bool:
#         # negtive integer
#         if n <= 0: return False
        
        # positive integer

        loop = []
        
        # loop in all sum
        while n >0 :
 
            su = 0
            # loop in integer
            for i in str(n):

                dig = int(i)
                su += dig ** 2
                
            if su == 1: return True
            loop.append(su)
            
            n = su
            # here wrong about first item 
            
            if len(loop) >1 and loop[0] == su: return False
            
        return False
            
                
            
        
        
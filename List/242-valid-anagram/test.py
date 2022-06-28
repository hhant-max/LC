class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        test if t and s can trasfer mutually, aka test their appearence occurance.
        '''
        
        # rule out the ocunts clash
        if len(s) != len(t): return False
        
        countS = {}
        countT = {}
        
        # construct hashmap based on string 
        for i in range(len(s)):
            countS[i] = 1 + countS.get(i,0)
            
        for j in range(len(t)):
            countT[i] = 1 + countS.get(i,0)
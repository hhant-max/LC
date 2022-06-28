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
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        # verify if they match
        for c in countS:
            # if there exists one clash
            if countS[c] != countT.get(c,0):
                return False
        
        return True
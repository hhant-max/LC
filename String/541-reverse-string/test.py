class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        leng = len(s)
        i = 0
        # 条件就无所谓了？
        while leng - 2*k*i <= 2*k:
            # reverse in k 
            res = leng - 2*k*i
            if res >= k:
                r = 2*k*i + k-1
            else:
                r = leng
            l = 2*k*i
            
            while l<r:
                s[l], s[r] = s[r],s[l]
                l +=1
                r -= 1
            i += 1
        return s
        
        
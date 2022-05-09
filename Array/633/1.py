class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # first find the biggest that square that bigger than 
        if c ==0: return True
        l,r = 0, c
        while l < r:
            mid = (l+r)//2
            if mid * mid > c:
                r = mid
            else:
                l = mid +1
                res = l 
            # but this is always the case 
            # if res* res < c and (res+1)*(res+1) > c:
            #     break

        # in this list find the combination
        available = res - 1
        for i in range(1,available+1):
            for j in range(i,available+1):
                # how to desingn if I gind anyone not everyone
                    if (i)**2 + (j)**2 == c:
                        return True

        return False
        

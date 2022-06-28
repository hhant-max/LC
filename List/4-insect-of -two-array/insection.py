class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        
        res = []
        
        for i in range(len(nums1)):
            count1[nums1[i]] = 1 + count1.get(nums1[i],0)
        for i in range(len(nums2)):
            count2[nums2[i]] = 1 + count2.get(nums2[i],0)
            
        for i in count1:
            if count1[i] > 0 and count2.get(i,0) > 0:
                res.append(i)
                
        return res 
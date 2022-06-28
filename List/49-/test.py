class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        group all the anagrams together
        '''
        res = defaultdict(list)
        
        # collect all string that're anagrams with string
        for s in strs:
            count = [0] * 26
            for ss in s:
                count[ord(ss) - ord('q')] += 1 # map them into value, then stored into a list
            
            # goup into res
            res[tuple(count)].append(s)
        return res.values()
        
            
            
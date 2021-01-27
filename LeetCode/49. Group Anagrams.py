# 2021-01-28
https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        # code1
        """
        for s in strs:
            ss = [ord(w) for w in s]  # ASCII-coded s that is key of dic
            ss.sort()                 # Tim sort
            ss = [chr(x) for x in ss] # re-characterizing
            ss = ''.join(ss)          # being list
            dic[ss].append(s)         # append into values list
          
        return dic.values()
        """
        
        # code2
        # not using ASCII code by using sorted function
        # which is can sort not only list but also "string"
        for s in strs:
            dic[''.join(sorted(s))].append(s)
          
        return dic.values()
        
        

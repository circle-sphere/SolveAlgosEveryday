# 2021-01-29
# https://leetcode.com/problems/regular-expression-matching/

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        re_result = re.match(p, s)
         # If s matches with p, it returns match object
         # Unless, it returns None
        
        if re_result != None:
            return sum(re_result.span()) == len(s)
            # span() method returns tuple about index of start and end of s that matches with p
            # if the sum of start and end idx is same to len(s), it means p covers whole s -> True
            # unless p covers only some part of s
        else:
            return False 
        

# 2021-01-21
# https://leetcode.com/problems/zigzag-conversion/

from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dic = defaultdict(str)

        i, k, trend = 0, 0, True
        # i is index of s
        # k is key of dic which is range(numRows)
        # trend represents that k is increasing or decreasing
        
        while i <= len(s)-1:
            if 0<=k and k<(numRows-1) and trend:
                # ex) 0 -> 1 -> 2, if numRows == 4
                dic[k] += s[i]
                i += 1
                k += 1
                if k == (numRows-1): trend = False

            elif 0<k and k<=(numRows-1) and not trend:
                # ex) 3 -> 2 -> 1
                dic[k] += s[i]
                i += 1
                k -= 1
                if k == 0: trend = True
            else: # case of numRows==1
                return s

        res = ''.join([dic[i] for i in range(numRows)])
        # preparing for python3.6- version to use ordered dict 

        return res
    

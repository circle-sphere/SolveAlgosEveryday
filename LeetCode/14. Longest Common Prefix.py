# 2021-01-31
# https://leetcode.com/problems/longest-common-prefix/

# Remember and review the usage of zip function with one input(*)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for tp in zip(*strs):
            if len(set(tp))!=1:
                return res
            else:
                res += tp[0]
        
        return res

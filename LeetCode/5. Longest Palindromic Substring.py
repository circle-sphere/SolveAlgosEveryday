# 2021-01-20
# https://leetcode.com/problems/longest-palindromic-substring/

# Using DP

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        dp_table = [[0]*len(s)  for _ in range(len(s))]

        res = ""
        for i in range(len(s)):
            dp_table[i][i] = 1
            res = s[i]

        maxLen = 1
        for i in range(len(s)-1, -1, -1): # from right
            for j in range(i+1, len(s)):  # from left          
                if s[i] == s[j]:          
                    if j-i == 1 or dp_table[i+1][j-1]:
                        # 한 칸 차이거나 안쪽이 회문이었다면
                        dp_table[i][j] = 1
                        if maxLen < j-i+1:
                            maxLen = j-i+1
                            res = s[i:j+1]

        return res

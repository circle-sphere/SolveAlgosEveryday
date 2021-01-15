# 2021-01-15
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Using defaultdict is key point.
# Let's study about collections library.

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_len = 0
        left, right = 0, 0
        window = defaultdict(int)
        
        while right < len(s):
            char = s[right]
            window[char] += 1
            
            while window[char] != 1:
                window[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
            
            
        

# 2021-01-30
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        num = 0
        previous = ''
        for i in range(len(s)):
            current = s[-(i+1)]
            
            if current == 'I' and previous in ['V', 'X']: # 4, 9
                num -= 1
            elif current == 'X' and previous in ['L', 'C']: # 40, 90
                num -= 10
            elif current == 'C' and previous in ['D', 'M']: # 400, 900
                num -= 100
            else:
                num += dic[current]

            previous = current

        return num
    

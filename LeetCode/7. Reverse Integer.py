# 2021-01-25
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        if x < 0:
            minus = True
        
        x = str(x).replace('-','')[::-1]
        
        if minus == True:
            x = int(x)*-1
        else:
            x = int(x)
                        
        if -2**31<=x and x <= 2**31-1:
            return x
        else:
            return 0

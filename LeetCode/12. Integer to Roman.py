# 2021-01-30
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        
        res = ""
        num_str = str(num)
        leng = len(num_str)
        for i in range(leng):
            div = divmod(int(num_str[-(i+1)]), 5)
            digit = 10**i
            
            if div[1] == 4:
                if div[0] == 0: # 4
                    res = dic[1*digit] + dic[5*digit] + res
                elif div[0] == 1: # 9
                    res = dic[1*digit] + dic[1*digit*10] + res    
            elif div[1] == 0: # 0, 5
                res = dic[5*digit]*div[0] + res
            elif div[1] in [1,2,3]:
                if div[0] == 0: # 1, 2, 3
                    res = dic[1*digit]*div[1] + res
                elif div[0] == 1: # 6, 7, 8
                    res = dic[5*digit] + dic[1*digit]*div[1] + res
        return res
                    
            
            

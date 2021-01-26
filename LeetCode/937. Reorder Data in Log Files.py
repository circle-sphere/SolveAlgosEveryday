# 2021-01-27
# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strs, nums = [], []
        for log in logs:
            if log.split()[1].isalpha():
                strs.append(log)
            else: # log.split()[1].isnum()
                nums.append(log)
                
        strs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return strs+nums

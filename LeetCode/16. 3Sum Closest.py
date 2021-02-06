# 2021-02-07
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = 0
        min_err = float('inf')
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                err = abs(target - sum3)

                if err < min_err:
                    min_err = err
                    res = sum3
                    
                if sum3 < target:
                    left += 1
                else:
                    #err >= min_err
                    right -= 1
            
            if err == 0:
                min_err = err
                res = sum3
                break

        return  res

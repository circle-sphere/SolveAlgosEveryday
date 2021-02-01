# 2021-02-02
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1, len(nums)-1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                
                if sum3 < 0:
                    left += 1
                elif sum3 > 0:
                    right -= 1
                else:
                    # sum3 == 0
                    res.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
        return res
        

# 2021-02-04
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        x = 1
        
        # Making cumulative product list from the left side
        for i in range(len(nums)):
            lst.append(x)
            x *= nums[i]
        
        # Making cumulative product from the right side and product them with lst
        x = 1
        for i in range(len(nums)-1,-1,-1):
            lst[i] = lst[i] * x
            x *= nums[i]
        
        return lst

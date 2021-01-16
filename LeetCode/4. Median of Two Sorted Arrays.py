# 2021-01-16
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    
    nums = nums1 + nums2
    nums.sort()
    
    leng = len(nums)
    if leng%2 == 1:
        med = nums[int(leng/2)]
    else:
        med = (nums[int(leng/2)] + nums[int(leng/2)-1])/2
        
    return med
            
            
        

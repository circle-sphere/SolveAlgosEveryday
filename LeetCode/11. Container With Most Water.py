# 2021-01-29
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        left_x, right_x = 0, len(height)-1
        
        while left_x != right_x:
            left_y, right_y = height[left_x], height[right_x]
            temp = abs(left_x - right_x) * min([left_y, right_y]) # volume of tempolary container
            if volume < temp: # update the volume largely
                volume = temp
            
            # Using two points method,
            # The objective is that finding large y values and get min y between them 
            if left_y < right_y:
                left_x += 1
            else: # left_y >= ight_y
                right_x -= 1
        
        return volume
        

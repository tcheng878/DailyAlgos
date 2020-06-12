class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > maxarea:
                maxarea = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxareaf
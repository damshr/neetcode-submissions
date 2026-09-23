class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers 
        left = 0
        right = len(heights) - 1
        res = 0 #store max area
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(res, area)
            # do not want smaller heights
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res


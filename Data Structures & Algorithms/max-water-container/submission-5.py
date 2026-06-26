class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximum = 0
        while l < r:
            if min(heights[l], heights[r]) * (r - l) > maximum:
                maximum = min(heights[l], heights[r]) * (r - l)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            
            
        return maximum
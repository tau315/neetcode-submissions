class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maximum = 0
        while i < j:
            if (j - i) * min(heights[i], heights[j]) > maximum:
                maximum = (j - i) * min(heights[i], heights[j])
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maximum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maximum = nums[0]
        for i in range(len(nums)):
            curr += nums[i]
            if nums[i] > curr:
                curr = nums[i]
            if curr > maximum:
                maximum = curr
        return maximum
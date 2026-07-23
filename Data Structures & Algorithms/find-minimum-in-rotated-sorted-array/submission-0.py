class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            middle = (i + j) // 2
            if nums[middle] > nums[j]:
                i = middle + 1
            else:
                j = middle
        return nums[i]
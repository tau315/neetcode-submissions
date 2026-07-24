class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[i]:
                if nums[middle] > target and nums[i] <= target:
                    j = middle
                else:
                    i = middle + 1
            else:
                if nums[middle] < target and nums[j] >= target:
                    i = middle + 1
                else:
                    j = middle

        return -1
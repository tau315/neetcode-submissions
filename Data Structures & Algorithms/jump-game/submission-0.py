class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        while i > 0:
            j = i - 1
            while j > -1:
                if nums[j] >= i - j:
                    i = j
                    break
                j -= 1
            if j == -1:
                return False
        return True
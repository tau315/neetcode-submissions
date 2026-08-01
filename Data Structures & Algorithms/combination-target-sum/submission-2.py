class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def combo(nums, i, target, curr, sol):
            if curr == target:
                ans.append(sol.copy())
            if curr > target:
                return
            for j in range(i, len(nums)):
                sol.append(nums[j])
                combo(nums, j, target, curr + nums[j], sol)
                sol.pop()
        combo(nums, 0, target, 0, [])
        return ans
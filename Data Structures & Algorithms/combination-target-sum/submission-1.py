class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def solutionSearch(start, remaining, curr):
            if remaining == 0:
                ans.append(curr.copy())
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if num > remaining:
                    continue
                curr.append(num)
                solutionSearch(i, remaining - num, curr)
                curr.pop()
        solutionSearch(0, target, [])
        return ans
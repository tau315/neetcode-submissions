class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def solutionSearch(nums, target, curr, sol):
            nonlocal ans
            if curr == target:
                ans.append(sol.copy())
                return
            if curr > target:
                return
            original_sol = sol.copy()
            for num in nums:
                sol.append(num)
                solutionSearch(nums, target, curr + num, sol.copy())
                sol.pop()
        solutionSearch(nums, target, 0, [])
        unique = set()

        for combination in ans:
            unique.add(tuple(sorted(combination)))
        
        return [list(combination) for combination in unique]
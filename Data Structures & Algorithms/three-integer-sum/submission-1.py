class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            target = -nums[i]
            m = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in m:
                    ans.append([nums[j], -target, target - nums[j]])
                else:
                    m[nums[j]] = 1
        m = {}
        answer = []
        for a in ans:
            if tuple(sorted(a)) not in m:
                answer.append(a)
                m[tuple(sorted(a))] = 1
        return answer
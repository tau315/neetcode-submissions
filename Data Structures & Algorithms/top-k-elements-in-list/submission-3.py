class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        mini = m[nums[0]]
        
        ans = []
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in m:
            freq[m[num]].append(num)
        for a in range(len(freq) - 1, 0, -1):
            for n in freq[a]:
                ans.append(n)
                if len(ans) == k:
                    return ans


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        counts = [[] for i in range(len(nums) + 1)]
        for ob in m.items():
            ke, v = ob
            counts[v].append(ke)
        ans = []
        i = len(counts) - 1
        while len(ans) < k and i > -1:
            if len(counts[i]) > 0:
                j = 0
                while len(ans) < k and j < len(counts[i]):
                    ans.append(counts[i][j])
                    j += 1
            i -= 1
        return ans




        


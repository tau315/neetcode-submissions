class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num, freq in m.items():
            frequencies[freq].append(num)
        ans = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


        


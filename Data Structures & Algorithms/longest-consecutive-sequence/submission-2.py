class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
        longest = 0
        for num in nums:
            length = 1
            if num - 1 not in m:
                while num + length in m:
                    length += 1
                longest = max(length, longest)
        return longest
        

        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = {}
        for num in nums:
            nums_map[num] = 1
        longest = 0
        for num in nums:
            if num - 1 not in nums_map:
                sequence = 0
                while num in nums_map:
                    num += 1
                    sequence += 1
                if sequence > longest:
                    longest = sequence
        return longest


        
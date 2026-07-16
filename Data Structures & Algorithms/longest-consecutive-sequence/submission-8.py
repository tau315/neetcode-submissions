class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = 1
        longest = 0
        maximum = 0
        for num in nums:
            longest = 1
            if num - 1 in m:
                pass
            else:
                while num + 1 in m:
                    num = num + 1
                    longest = longest + 1
                if longest > maximum:
                    maximum = longest
        return maximum
            


        
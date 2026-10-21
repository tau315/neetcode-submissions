class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 1
        longest = 0
        s_map = {}
        s_map[s[0]] = 0
        while r < len(s):
            if s[r] in s_map:
                if r - l > longest:
                    longest = r - l 
                l = max(l, s_map[s[r]] + 1)
                s_map[s[r]] = r
                r += 1
            else:
                s_map[s[r]] = r
                r += 1
        return max(longest, r - l)
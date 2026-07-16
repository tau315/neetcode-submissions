class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_longest = 0
        longest = 0
        i = 0
        j = 0
        m = {}
        while j < len(s):
            if s[j] in m:
                if current_longest > longest:
                    longest = current_longest
                i = max(i, m[s[j]] + 1)
                m[s[j]] = j
                
                j = j + 1
                current_longest = j - i
                
                
            else:
                m[s[j]] = j
                j = j + 1
                current_longest = current_longest + 1
                if current_longest > longest:
                    longest = current_longest
        return longest

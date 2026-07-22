class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        m = {}
        current = 0
        longest = 0
        while j < len(s):
            if s[j] not in m:
                m[s[j]] = j
                current += 1
                if current > longest:
                    longest = current
                j += 1
            else:
                last_index = m[s[j]]
                while i < last_index + 1:
                    del m[s[i]]
                    i += 1
                current = j - i + 1
                m[s[j]] = j
                j += 1
        return longest
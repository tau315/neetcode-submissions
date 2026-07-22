class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        m = {}
        current_most_chars = 0
        longest = 0
        while j < len(s):
            if s[j] in m:
                m[s[j]] += 1
            else:
                m[s[j]] = 1
            current_most_chars = max(m[s[j]], current_most_chars)
            if j - i + 1 - k > current_most_chars:
                while j - i + 1 - k > current_most_chars:
                    m[s[i]] -= 1
                    i += 1
                current_most_chars = j - i + 1 - k
            if j - i + 1 > longest:
                longest = j - i + 1
            j += 1
        return longest

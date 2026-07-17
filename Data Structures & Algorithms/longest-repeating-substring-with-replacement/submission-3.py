class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        m = {}
        longest = 0
        cur_longest = 0
        
        while j < len(s):
            if s[j] in m:
                m[s[j]] += 1
            else:
                m[s[j]] = 1
            cur_longest = max(cur_longest, m[s[j]])
            j += 1
            while (j - i) - cur_longest > k:
                m[s[i]] -= 1
                i += 1
            longest = max(longest, j - i )
        return longest

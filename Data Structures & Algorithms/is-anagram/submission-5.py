class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_m = {}
        for c in s:
            if c in s_m:
                s_m[c] += 1
            else:
                s_m[c] = 1
        t_m = {}
        for c in t:
            if c in t_m:
                t_m[c] += 1
            else:
                t_m[c] = 1
        if s_m == t_m:
            return True
        return False
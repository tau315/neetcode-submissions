class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_m = {}
        for char in t:
            if char in t_m:
                t_m[char] += 1
            else:
                t_m[char] = 1
        i = 0
        j = 0
        s_m = {}
        shortest = len(s) + 1
        shortest_i = 0
        satisfied = 0
        required = len(t_m)
        while j < len(s):
            if s[j] in s_m:
                s_m[s[j]] += 1
            else:
                s_m[s[j]] = 1
            if s[j] in t_m and s_m[s[j]] == t_m[s[j]]:
                satisfied += 1
            
            while satisfied == required:
                s_m[s[i]] -= 1
                if s[i] in t_m and s_m[s[i]] < t_m[s[i]]:
                    satisfied -= 1
                    if j - i + 1 < shortest:
                        shortest = j - i + 1
                        shortest_i = i
                i += 1

            j += 1
        if shortest == len(s) + 1:
            return ""
        return s[shortest_i: shortest_i + shortest]




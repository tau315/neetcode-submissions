class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window = {}
        perm = {}
        for i in range(len(s1)):
            perm[s1[i]] = perm.get(s1[i], 0) + 1
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        for i in range(len(s1), len(s2)):
            if window == perm:
                return True
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == perm:
            return True
        return False

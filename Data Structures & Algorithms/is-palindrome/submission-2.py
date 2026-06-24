class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if self.alphaNum(s[l]) and self.alphaNum(s[r]):
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            if not self.alphaNum(s[l]):
                l += 1
            if not self.alphaNum(s[r]):
                r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
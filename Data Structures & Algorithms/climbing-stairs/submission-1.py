class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        x = 1
        y = 2
        for i in range(n - 2):
            z = x
            x = y
            y = z + y
        return y
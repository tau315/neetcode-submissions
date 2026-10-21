class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        ans = [0 for i in range(len(temperatures))]
        for j in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[j]:
                index = stack.pop()
                ans[index] = j - index
            stack.append(j)
        return ans
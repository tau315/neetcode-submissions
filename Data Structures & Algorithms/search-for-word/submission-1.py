class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starting = word[0]
        starting_points = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == starting:
                    starting_points.append((i, j))
        
        def dfs(curr, visited, target):
            if curr in visited:
                return False
            if curr[0] == -1 or curr[0] == len(board) or curr[1] == -1 or curr[1] == len(board[0]):
                return False
            if board[curr[0]][curr[1]] == target[0]:
                if len(target) == 1:
                    return True
                visited.append((curr[0], curr[1]))
                return dfs((curr[0] + 1, curr[1]), visited.copy(), target[1:]) or dfs((curr[0] - 1, curr[1]), visited.copy(), target[1:]) or dfs((curr[0], curr[1] + 1), visited.copy(), target[1:]) or dfs((curr[0], curr[1] - 1), visited.copy(), target[1:])
        ans = False
        for start in starting_points:
            ans = ans or dfs(start, [], word)
        return ans
                 
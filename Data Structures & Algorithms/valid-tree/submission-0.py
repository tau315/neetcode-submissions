class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = {}
        def dfs(node, parent):
            if node in seen and parent != seen[node]:
                return False
            seen[node] = parent
            result = True
            for n in graph[node]:
                if n == parent:
                    continue
                result = dfs(n, node) and result
            return result
        result = dfs(0, None)
        if len(seen) != n:
            return False
        return result
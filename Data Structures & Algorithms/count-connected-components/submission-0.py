class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        graph = { i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node):
           for neigh in graph[node]:
                if not neigh in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        components = 0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components += 1
        
        return components

        


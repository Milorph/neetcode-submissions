class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = { i : [] for i in range(len(edges) + 1)}


        def dfs(node, parent, visited):
            if node in visited:
                return False
            
            visited.add(node)

            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node, visited):
                    return False
            return True

        for u, v in edges:

            visited = set()

            graph[u].append(v)
            graph[v].append(u)

            if not dfs(u, -1, visited):
                return [u,v]

        return []
            

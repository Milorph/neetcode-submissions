class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = { i : [] for i in range(len(edges) + 1)}


        def dfs(node, parent, visited):
            if node in visited:
                return True
            
            visited.add(node)

            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node, visited):
                    return True
            return False

        for u, v in edges:

            visited = set()

            graph[u].append(v)
            graph[v].append(u)

            if dfs(u, -1, visited):
                return [u,v]

        return []
            

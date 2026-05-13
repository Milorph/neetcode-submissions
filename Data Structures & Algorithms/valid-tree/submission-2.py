class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        visited = set()

        mapping = { i : [] for i in range(n)}

        for node, edge in edges:
            mapping[node].append(edge)
            mapping[edge].append(node)

        def dfs(node, parent):
            
            if node in visited:
                return False
            
            
            visited.add(node)
            for edge in mapping[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node):
                    return False
            

            return True
        
        if not dfs(0, -1):
            return False
        
        
        return len(visited) == n


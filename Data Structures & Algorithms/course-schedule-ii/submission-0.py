class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        visiting = set()
        mapping = { i: [] for i in range(numCourses)}

        order = []

        for crs, pre in prerequisites:
            mapping[crs].append(pre)

        def dfs(course):
            
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for pre in mapping[course]:
                if not dfs(pre):
                    return False
            
            
            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order

        

            

        
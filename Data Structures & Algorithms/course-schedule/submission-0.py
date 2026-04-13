class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        al = {i:[] for i in range(numCourses)}
        for crs, dep in prerequisites:
            al[crs].append(dep)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if al[crs] == []:
                return True
            
            visited.add(crs)
            for c in al[crs]:
                if not dfs(c): return False
            visited.remove(crs)
            al[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
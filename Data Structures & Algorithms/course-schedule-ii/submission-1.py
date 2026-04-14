class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = {i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            hm[x].append(y)
        
        visiting = set()
        finished = set()
        order = []

        def dfs(curr):
            if curr in visiting:
                return False
            
            if curr in finished:
                return True
            
            visiting.add(curr)

            for c in hm[curr]:
                if not dfs(c):
                    return False

            visiting.remove(curr)
            finished.add(curr)
            order.append(curr)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
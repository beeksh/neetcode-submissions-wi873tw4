class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        hm = {i:[] for i in range(n)}
        for x,y in edges:
            hm[x].append(y)
            hm[y].append(x)
        
        visited = set()

        def dfs(curr, prev):
            if curr!=prev and curr in visited:
                return False

            visited.add(curr)
            for x in hm[curr]:
                if x == prev:
                    continue
                if not dfs(x, curr): 
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(visited) == n
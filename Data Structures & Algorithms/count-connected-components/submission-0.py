class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hm = {i:[] for i in range(n)}
        for x,y in edges:
            hm[x].append(y)
            hm[y].append(x)

        visited = set()

        def dfs(curr):
            visited.add(curr)

            for x in hm[curr]:
                if x in visited:
                    continue
                dfs(x)
        

        count = 0
        for i in range(n):
            if i in visited:
                continue
            count +=1
            dfs(i)
        
        return count 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q  = deque()

        def ad(r,c):
            if (r<0 or r>=rows or
                c<0 or c>=cols or
                grid[r][c] != 1
            ):
                return False
            grid[r][c] = 2
            q.append([r,c])
            return True

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])        

        time = 0

        while q:
            changed = False
            
            for i in range(len(q)):
                
                r,c = q.popleft()
                changed |= ad(r+1,c)
                changed |= ad(r-1,c)
                changed |= ad(r,c+1)
                changed |= ad(r,c-1)

            if changed:
                time+=1
        for r in grid:
            if 1 in r:
                return -1
        
        return time
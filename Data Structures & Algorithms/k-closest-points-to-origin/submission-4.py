class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            a = points[i][0]
            b = points[i][1]
            d = math.sqrt(a*a + b*b)
            heapq.heappush(heap, (d, [a,b]))

        x = heapq.nsmallest(k,heap)
        out = []
        for i in x:
            out.append(i[1])
        return out
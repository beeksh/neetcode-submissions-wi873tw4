class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap,-s)
        while len(heap)>1:
            a, b = - heapq.heappop(heap), - heapq.heappop(heap)
            if a == b:
                continue
            else:
                heapq.heappush(heap, -abs(a-b))
        if heap:
            return -heap[0]
        else:
            return 0

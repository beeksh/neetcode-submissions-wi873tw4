class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = Counter(tasks)
        print(x.values())
        heap = []
        for i in x.values():
            heapq.heappush(heap, -i)
        q = deque()
        t=0

        while heap or q:
            t+=1
            if heap:
                x = 1+ heapq.heappop(heap)
                if x:
                    q.append([x, t+n])
            if q and q[0][1]==t:
                temp = q.popleft()
                heapq.heappush(heap, temp[0])
        return t
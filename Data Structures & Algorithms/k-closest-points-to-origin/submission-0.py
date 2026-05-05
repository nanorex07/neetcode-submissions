class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda p: p[0]**2 + p[1]**2
        
        heap = []
        for point in points:
            heapq.heappush(
                heap, (-dist(point), point)
            )
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [k[1] for k in heap]
    
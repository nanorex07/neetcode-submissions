class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        count = [0]*n

        allocations = []
        avail = [i for i in range(n)]

        for start, end in meetings:
            while allocations and allocations[0][0] <= start:
                _, room = heapq.heappop(allocations)
                heapq.heappush(avail, room)
            
            if not avail:
                end_time, room = heapq.heappop(allocations)
                end = end_time + end - start
                heapq.heappush(avail, room) 

            room = heapq.heappop(avail)
            heapq.heappush(allocations, [end, room])
            count[room]+=1

        return count.index(max(count))

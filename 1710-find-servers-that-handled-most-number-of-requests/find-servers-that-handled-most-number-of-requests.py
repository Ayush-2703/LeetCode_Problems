import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Keeps track of free servers sorted by server id
        available = SortedList(range(k))
        # Min-heap storing (end_time, server_id)
        busy = []
        # Request count per server
        request_count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # 1. Free all servers that have finished before or at current arrival time
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)

            # 2. If no servers are available, drop the request
            if not available:
                continue

            # 3. Find the server with id >= (i % k)
            target = i % k
            idx = available.bisect_left(target)
            
            # If none >= target, wrap around to the first available server
            if idx == len(available):
                idx = 0
            
            chosen_server = available.pop(idx)
            
            # 4. Assign request to chosen_server
            request_count[chosen_server] += 1
            heapq.heappush(busy, (start + duration, chosen_server))

        # Find servers with the maximum count
        max_handled = max(request_count)
        return [srv for srv, cnt in enumerate(request_count) if cnt == max_handled]
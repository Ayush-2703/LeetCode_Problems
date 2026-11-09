import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        request_count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)

            if not available:
                continue

            target = i % k
            idx = available.bisect_left(target)

            if idx == len(available):
                idx = 0
            
            chosen_server = available.pop(idx)

            request_count[chosen_server] += 1
            heapq.heappush(busy, (start + duration, chosen_server))

        max_handled = max(request_count)
        return [srv for srv, cnt in enumerate(request_count) if cnt == max_handled]
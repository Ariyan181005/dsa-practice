import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):

            # Release servers that have completed their requests
            while busy and busy[0][0] <= start:
                end, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find the first available server >= i % k
            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            count[server] += 1
            heapq.heappush(busy, (start + duration, server))

        max_requests = max(count)

        return [i for i in range(k) if count[i] == max_requests]
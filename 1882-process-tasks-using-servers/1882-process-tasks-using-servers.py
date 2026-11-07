class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = []
        heapq.heapify(free_servers)
        busy_servers = []
        heapq.heapify(busy_servers)
        for i in range(len(servers)):
            s = servers[i]
            heapq.heappush(free_servers, (s, i))
        order = []
        for i in range(len(tasks)):
            task = tasks[i]
            while busy_servers and busy_servers[0][0] <= i:
                serv = heapq.heappop(busy_servers)
                serv_weight = serv[1]
                serv_idx = serv[2]

                heapq.heappush(free_servers, (serv_weight, serv_idx))
            if free_servers:
                serv = heapq.heappop(free_servers)
                serv_weight = serv[0]
                serv_idx = serv[1]

                next_free = i + task
                heapq.heappush(busy_servers, (next_free, serv_weight, serv_idx))
                order.append(serv_idx)
            else:
                serv = heapq.heappop(busy_servers)
                serv_next_free = serv[0]
                serv_weight = serv[1]
                serv_idx = serv[2]

                next_free = serv_next_free + task
                heapq.heappush(busy_servers, (next_free, serv_weight, serv_idx))
                order.append(serv_idx)        
        return order   
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # flights[i] -> contains start, end, price
        # src = starting airport
        # dst = destination airport
        # k is max number of stop in the middle (not including start, dest)
        
        # need adj list first
        adj = [[] for _ in range(n)]
        output = [float('inf') for _ in range(n)] # min cost to get to each city
        output[src] = 0

        for u, v, w in flights:
            adj[u].append((v,w))
        
        graph = deque()
        graph.append((src, -1, 0))
        while graph:
            u, stop, cost = graph.popleft()
            # check if the number of stops we made is greater than or equal to maxstops
            if stop >= k:
                continue
            for v, w in adj[u]:
                if cost + w < output[v]:
                    output[v] = cost + w 
                    graph.append((v, stop + 1, cost+w))
        if output[dst] == float('inf'):
            return -1
        return output[dst]
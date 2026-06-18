class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        visited = set()

        for edge in edges:
            print(edge[0], edge[1])
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        print(graph)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res
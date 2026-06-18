class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)

        # fully connected, no cycles

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        def dfs(node, parent):
            print(node, visited)
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n # make sure we visit everything
        

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # pacific - everything that can be reached from the pacific ocean
        # atlantic - everything that can be reached from the atlantic ocean

        # run bfs to add the cells to visited for each one
        # at the end find the intersection between the two
        rows, cols = len(heights), len(heights[0])
        pacificvisited = [[False for _ in range(cols)] for _ in range(rows)]
        atlanticvisited = [[False for _ in range(cols)] for _ in range(rows)]

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ps = set()
        ats = set()

        def bfs(source, ocean): # take the current ocean we're running on and the current coordinate
            # only add the neighbor if its lower than the curr one and dont add if its more
            q = deque()
            q.append(source)
            while q:
                curr = q.popleft()
                ocean[curr[0]][curr[1]] = True
                for dr, dc in directions:
                    newr = curr[0] + dr
                    newc = curr[1] + dc
                    if newr < rows and newc < cols and newr >= 0 and newc >= 0 and ocean[newr][newc] == False and heights[newr][newc] >= heights[curr[0]][curr[1]]:
                        q.append((newr,newc))

        res = []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    ps.add((r,c))
                if r == rows - 1 or c == cols - 1:
                    ats.add((r,c))
        
        for pacificSource in ps:
            bfs(pacificSource, pacificvisited)
        for aSource in ats:
            bfs(aSource, atlanticvisited)
        
        for r in range(rows):
            for c in range(cols):
                if pacificvisited[r][c] == 1 and atlanticvisited[r][c] == 1:
                    res.append((r,c))
        
        return res


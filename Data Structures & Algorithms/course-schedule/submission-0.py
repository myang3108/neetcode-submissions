class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to see if we have a cycle in our directed graph
        # a -> b means that b is a prereq of a
        # make an adj list and then do a traversal of the graph and if we have a visited node then return false
        # otherwise return true at the end

        # adj list means for every node, we get the neighbors of it - a defaultdict of lists
        adjlist = defaultdict(list)
        for u, v in prerequisites:
            adjlist[u].append(v)
        
        visited = set() # list of courses we are currently visitng in our dfs
        def dfs(node):
            
            if node in visited:
                return False
            # case where the node has no prereqs
            if adjlist[node] == []:
                return True
                
            # otherwise run dfs on each of the neighbors and add em to visited
            # first mark the current node as visited
            visited.add(node)
            for nei in adjlist[node]:
                if not dfs(nei):
                    return False # if one of them is false we can stop it immedietley dont need to finish all of them
            # now we are no longer visitng this course so we remove it
            visited.remove(node)
            adjlist[node] = [] # we dont have to do it again in the future if we have to rerun        
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
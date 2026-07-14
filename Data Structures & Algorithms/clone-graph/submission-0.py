"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # go through each node - skip if we've already cloned
        # have a mp[node] = new cloned node
        # for the node go through the neighbors of the og and attach them accordingly
        mp = {}

        def dfs(node):
            if node in mp:
                return mp[node]

            copy = Node(node.val)
            mp[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        if node is None:
            return None

        return dfs(node)

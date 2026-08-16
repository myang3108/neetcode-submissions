class Solution:
    def hasPathSum(self, root, targetSum):
        def helper(root, sumleft):
            if root is None: # check if the tree is empty
                return False
            
            remaining = sumleft - root.val   # subtract BEFORE checking
            
            if root.left is None and root.right is None:
                return remaining == 0
            
            return helper(root.left, remaining) or helper(root.right, remaining)
        
        return helper(root, targetSum)
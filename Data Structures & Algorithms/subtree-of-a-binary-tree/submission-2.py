# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot) == True:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def sameTree(self, tree1, tree2):
                if (tree1 == None and tree2 != None) or (tree1 != None and tree2 == None):
                    return False
                if (tree1 == None and tree2 == None):
                    return True
                return (tree1.val == tree2.val) and self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)

        
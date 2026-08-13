# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPath(self,node,target):
        if node is None:
            return 0

        target-=node.val
        count=0

        if target == 0:
            count=1   

        count+=self.findPath(node.left,target)
        count+=self.findPath(node.right,target)

        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        count=self.findPath(root,targetSum)    

        count+=self.pathSum(root.left,targetSum)
        count+=self.pathSum(root.right,targetSum)

        return count                                                                               

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len=0

        def dfs(node,left,right):
            self.max_len=max(self.max_len,left,right)

            #Move LEFT  → previous value of RIGHT + 1
            if node.left:
                dfs(node.left,right+1,0)

            #Move RIGHT → previous value of LEFT + 1
            if node.right:
                dfs(node.right,0,left+1)    

        dfs(root,0,0)

        return self.max_len






        

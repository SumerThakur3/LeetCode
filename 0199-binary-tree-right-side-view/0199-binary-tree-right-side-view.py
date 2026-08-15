# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        queue=[root]

        while queue:
            # Number of nodes in the current level
            level_size=len(queue)

            for i in range(level_size):
                # Take the first node from the queue
                node=queue.pop(0)

                # If it is the last node of this level,
                # it is visible from the right side
                if i == level_size-1:
                    res.append(node.val)

                # Add left and right child to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res                




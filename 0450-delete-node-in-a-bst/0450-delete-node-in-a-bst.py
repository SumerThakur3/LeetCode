class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:        
    def deleteNode(self, root, key):
        if root is None:
            return None
        # Step 1: Search
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            temp = self.findMin(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        
        return root
    
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
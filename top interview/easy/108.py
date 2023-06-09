class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)



class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None
            
            # always choose right middle node as a root
            p = (left + right) // 2 
            if (left + right) % 2:
                p += 1 

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
'''
my approach is to recursive traverse the tree if it is not root return none.
and declare a local variable to record the length
'''

'''
The actual apparoach is to use recursion to get the maximum length each time and at the end when return it, we just return the maximum
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)
        return max(left_length,right_length)+1
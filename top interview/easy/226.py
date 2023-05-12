class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return None
    
    right = invertTree(root.right)
    left = invertTree(root.left)
    root.left = right
    root.right = left
    return root

if __name__ == "__main__":
    root =TreeNode ([4,2,7,1,3,6,9])
    
    print(invertTree(root))
class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
    
    traverse(root)
    return result

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(postorder_traversal(root))  

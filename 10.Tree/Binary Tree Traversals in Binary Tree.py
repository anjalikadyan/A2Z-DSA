from sys import *
from collections import *
from math import *

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.data)
        inorder_traversal(root.right, result)

def preorder_traversal(root, result):
    if root:
        result.append(root.data)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)

def postorder_traversal(root, result):
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.data)

def getTreeTraversal(root):
    inorder_result = []
    preorder_result = []
    postorder_result = []
    
    inorder_traversal(root, inorder_result)
    preorder_traversal(root, preorder_result)
    postorder_traversal(root, postorder_result)
    
    return [inorder_result, preorder_result, postorder_result]

if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    
    traversals = getTreeTraversal(root)
    print("In-order Traversal:", traversals[0])
    print("Pre-order Traversal:", traversals[1])
    print("Post-order Traversal:", traversals[2])

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        li = []
        li.po
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def post_order_traversal(self,tree, result):
        if tree:
            result = self.post_order_traversal(tree.left, result)
            result = self.post_order_traversal(tree.right, result)
            result += (str(tree.value)) + ","
        
        return result
            
        
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.post_order_traversal(tree.root, ""))
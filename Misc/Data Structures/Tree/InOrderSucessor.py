class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_successor_bst(root, d):
        list = inorder_successor_bst(root.left)
        list.append(root.val)
        list = inorder_successor_bst(root.right)
        return list

inorder_successor_bst()



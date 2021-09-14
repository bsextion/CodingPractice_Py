class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = traverse(root, [])
        return result


def traverse(root, list):
    if root:
        list = traverse(root.left, list)
        list.append(root.val)
        list = traverse(root.right, list)
    return list
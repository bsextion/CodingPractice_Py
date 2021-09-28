class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def has_path(root, sum):
    allPaths = []
    findPaths(root,sum, "", allPaths)

def findPaths(root, sum,path, allPaths):

    if root:
        if root.val == sum and root.right is None and root.left is None:
            allPaths.append(path)
        if sum < 0:
            return ""
        path = has_path(root.left, sum-root.val)
        path = str(root.val) + ""
        path = has_path(root.right, sum - root.val)
    return

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("Tree has path: " + str(has_path(root, 23)))
print("Tree has path: " + str(has_path(root, 16)))
  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true

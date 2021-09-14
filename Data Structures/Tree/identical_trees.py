class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = None


def are_identical(root1:BinaryTreeNode, root2:BinaryTreeNode):
  word_left = depth_first(root1, "")
  word_right = depth_first(root2, "")
  if word_left == word_right:
      return True
  else:
      return False

def depth_first(root, word):
    if root:
        word = depth_first(root.left, word)
        word += "" + str(root.data)
        word = depth_first(root.right, word)
    return word

root1 = BinaryTreeNode(6)
root2 = BinaryTreeNode(6)
root1.left = BinaryTreeNode(4)
root2.left = BinaryTreeNode(4)
root1.right = BinaryTreeNode(7)
root1.right = BinaryTreeNode(7)
are_identical(root1, root2)


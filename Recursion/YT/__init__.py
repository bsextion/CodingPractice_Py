class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def level_order_traversal(root):
    traverse(root)

def traverse(root):
    if root == None:
        return

    if root.left == None and root.right == None:
        print(str(root.val) + " ")
        return

    if root.left is not None:
        traverse(root.left)

    if root.right is not None:
        traverse(root.right)
    print(str(root.val))

tree = Tree(100)
tree.left = Tree(80)
tree.left.left = Tree(50)
tree.left.right = Tree(90)
tree.right = Tree(120)
tree.right.left = Tree(110)
tree.right.right = Tree(140)
level_order_traversal(tree)



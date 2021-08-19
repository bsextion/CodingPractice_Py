from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = Node(root)


def lev_order_traversal(root):
    queue = deque()
    stack = deque()
    queue.append(root)
    result = ""

    while (len(queue) > 0):
        curr = queue.popleft()
        result += str(curr.data) + ","
        stack.append(curr.data)

        queue.append(curr.left) if curr.left else queue
        queue.append(curr.right) if curr.right else queue

    while (len(stack) > 0):
        data = stack.pop()
        result += str(data) + ","
    print(result)


tree = Tree(12)
tree.left = Node(7)
tree.right = Node(1)
tree.left.left = Node(9)
tree.right.left = Node(10)
tree.right.right = Node(5)

lev_order_traversal(tree.root)


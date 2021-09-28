# In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
# Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
# After removing each node from the queue, insert both of its children into the queue.
# If the queue is not empty, repeat from step 3 for the next level.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    depth = 0

    while len(queue) > 0:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    traverse(root)

main()
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # def goodNodes(self, root, count):
    #     #if tree is null, return
    #     if root and (root.left or root.right):
    #         prev_left = self.goodNodes(root.left, count)
    #         if prev_left.val > root.val:
    #             count += 1
    #         prev_right = self.goodNodes(root.right, count)
    #         if prev_right.val > root.val:
    #             count += 1
    #     return root

    def goodNodes(self, tree):
        self.num = 0
        self.traverse(tree,pow(2,-31))
        return self.num

    def traverse(self, root, count):
        if root is None:
            return

        if root.val >= count:
            self.num += 1
            count = max(root.val, count)

        self.traverse(root.left, count)
        self.traverse(root.right,count)

        return self.num



root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

problem = Solution()
print(problem.goodNodes(root))



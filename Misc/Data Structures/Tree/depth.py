# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # class Solution:
# #     def inorderTraversal(self, root):
# #         depth = traverse(root)
# #         return depth
#
#
# class Solution:
#     def maxDepth(self, root) -> int:
#         curr_level_lst = []
#
#     child_level_lst = [[root]]
#     curr_level_lst.append(root)
#
#     while len(curr_level_lst) > 0:
#         temp = []
#         for node in curr_level_lst:
#             if node.left:
#                 temp.append(node.left)
#             if node.right:
#                 temp.append(node.right)
#             child_level_lst.append(temp) if len(temp) > 0 else child_level_lst
#         curr_level_lst = temp
#     return len(child_level_lst)
#
#
# # for each value in current level, add to temp and add to result list
# # add copy the temp to current level
#
#
# # return size of result list
#
# # def traverse(root):
# #     if root is None:
# #         return -1
# #
# #     left_height = traverse(root.left)
# #     right_height = traverse(root.right)
# #
# #     return 1 + max(left_height,right_height)
#
#
# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
#
# height(tree)

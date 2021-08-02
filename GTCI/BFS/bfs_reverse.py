

from collections import deque
#parent queue, children array, result array
#push root into parent queue
#while parent queue is not empty
#for size of parent queue
#get the children for each memeber in parent queue and add to child array
#append the result array with the child array
#put all the children in the parent queue
#repeat until parent queue is empty

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  child_queue, child_arr, parent_queue, result, result_final = deque(), [], deque(), deque(), []
  result_queue = deque()
  parent_queue.append(root)
  result.append([root.val])
  
  while(len(parent_queue) > 0):
    for parent in parent_queue:
        if parent.left:
          child_queue.append(parent.left)
        if parent.right:
          child_queue.append(parent.right)
          
    for child in child_queue:
      child_arr.append(child.val)         
    
    if len(child_arr) == 0:
      break  
      
    result.append(child_arr)
      
    child_arr = []
    parent_queue.clear()
    parent_queue = deque(child_queue)
    child_queue.clear()
    
  while len(result) > 0:
      arr = result.pop()
      result_final.append(arr)
          
  return result_final


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)    
  print("Level order traversal: " + str(traverse(root)))


main()



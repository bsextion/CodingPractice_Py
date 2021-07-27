class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST(object):
    def __init__(self, root):
        self.root = Node(root)
         
    def insert(self, new_val):
        curr_node = self.root
        while(curr_node):
            if new_val < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = Node(new_val)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = Node(new_val)
                    break
                else:
                    curr_node = curr_node.left
                              
        return
    
    def is_bst_satisfied(self):
        return self.traverse(self.root, [], 0)

    def traverse(self, curr, arr, idx):
        if curr:
            self.traverse(curr.left, arr, idx)
            arr.append(curr.data)
            if len(arr) > 1:
                if arr[idx] > arr[idx+1]:
                    idx += 1
                    return False 
            self.traverse(curr.right, arr, idx)
        return True            
  
        
bst = BST(10)
bst.insert(3)
bst.insert(1)
print(bst.is_bst_satisfied())
        
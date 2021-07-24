class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next    
    
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node
    
  def merge_sorted(self, llist):
     #assign list to two values
     left_list = self.head
     right_list = llist.head
     
     #assign nodePointer a value
     pointer_list = Node(None)
     
     if left_list is None:
         return right_list
     if right_list is None:
         return left_list
     
     if left_list and right_list: #if list1 and list2 (set the intial pointer)
         if left_list.data <= right_list.data:
             pointer_list = left_list
             left_list = left_list.next
         else:
             pointer_list = right_list
             right_list = right_list.next     
     
     new_head = pointer_list
     #while list1 and list2
     while left_list and right_list:
        if (left_list.data <= right_list.data):
         pointer_list.next = left_list
         pointer_list = pointer_list.next
         if left_list.next:
             left_list = left_list.next
         else: 
             left_list = None    
        else:
         pointer_list.next = right_list
         pointer_list = pointer_list.next
         if right_list.next:
             right_list = right_list.next
         else:
             right_list = None                
                
     #while list1
     while left_list:
         pointer_list.next = left_list
         pointer_list = pointer_list.next
         if left_list.next:
             left_list = left_list.next
         else: 
             left_list = None 
     
     #while lists2
     while right_list:
         pointer_list.next = right_list
         pointer_list = pointer_list.next
         if right_list.next:
             right_list = right_list.next
         else:
             right_list = None
             
     #return 
     self.head = new_head
     return pointer_list
  
     
     
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()       
     
      
      
      
          
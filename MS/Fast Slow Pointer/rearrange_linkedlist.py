class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()

def reorder(head):
  middle = find_middle(head)
  reversed_middle = reverse_middle(middle)
  ptr_head = head
  head = head.next

  while(head):
    pass



  #while reverse_middle
  #temp to hold the next values: ptr_head.next
  #ptr.head = middle
  #ptr.head.next = temp

  #reverse_middle = reverse_middle.next


  #have a pointer pointing to the middle of the list
  #reverse the second half of the linked list using recursion
  #start from the begininng, place after node, move the node to the next
  # TODO: Write your code here
  return

def reverse_middle(head):
  if head is None or head.next is None:
    return head
  p = reverse_middle(head.next)
  head.next.next = head
  head.next = None
  return p


def find_middle(head):
  slow_pointer = head
  fast_pointer = head

  while fast_pointer:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
  return slow_pointer


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
reorder(head)

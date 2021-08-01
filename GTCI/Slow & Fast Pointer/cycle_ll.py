#create a slow and fast pointer pointing to head
#fast pointer will move two steps
#slow pointer moves one step
#if fast pointer equals slow pointer at any point, return true
#continue while both fast pointer isn't null AND slow pointer isn't null

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  fast_pointer = head
  slow_pointer = head
  fast_count = 0
  slow_count = 0
  length = 0

  while not fast_pointer is None and not slow_pointer is None:
      fast_pointer = fast_pointer.next.next
      slow_pointer = slow_pointer.next
      fast_count += 2
      slow_count += 1
      if fast_pointer == slow_pointer:
          length = fast_count - slow_count
          return True 
  
  length = fast_count - slow_count
  return False


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()
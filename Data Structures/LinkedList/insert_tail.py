class LinkedList(head=None):
    def __init__(self, head):
        self.head = None
    def append(self):
        if


class Node(data=None, next=None):
    def __init__(self,data,next):
        self.data = data
        self.next = next

def insert_at_tail(lst:LinkedList, value):
    head = lst.head
    if lst.head == None:
        lst.head = Node(value)
        return
    else:
        lst = lst.head
        while lst.next:
            lst = lst.next
        lst.next = Node(value)
        return



linkedlist = LinkedList()
linkedlist.head = Node(6)
linkedlist.head.next = Node(7)
linkedlist.head.next.next = Node(8)
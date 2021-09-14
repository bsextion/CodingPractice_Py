#REVIEW
class LinkedList:
    def __init__(self, node=None):
        self.head = Node(node)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node
        return

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def search(lst, value):
    curr = lst.head
    while not curr is None:
        if curr.data == value:
            return True
        else:
            curr = curr.next

    return False
#curr = lst.head
#if the head.next and head.next.data = value
#prev = head
#curr_next = head.next.next
#prev.next

#else
#curr = curr.next
def detect_loop(lst):
    if not lst.head:
        return lst

    ptr = lst.head
    ptr2 = lst.head.head

    while (not ptr is None):
            if ptr.next and ptr2.next.next:
                if ptr == ptr:
                    return True
                else:
                    ptr = ptr.next
                    ptr2 = ptr2.next.next
            else:
                return False
    return False


ll = LinkedList(5)
ll.append(90)
ll.append(10)
ll.append(4)

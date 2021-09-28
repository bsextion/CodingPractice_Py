# This is an input class. Do not edit.
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    if not linkedList:
        return linkedList
    head = linkedList
    #map to store occuences of values
    map = dict()
    map[linkedList.value] = 1
    prev = linkedList
    current = linkedList.next
    while current:
        key = current.value
        if key in map:
            if prev.next:
                prev.next = prev.next.next
                current = prev.next
            else:
                prev.next = None
        else:
            map[key] = 1
            current = current.next
            prev = prev.next

    #while current node isn't empty

    #if the data in current node is already in the map,
    #if next is not None, curent.next = current.next.next
    #else, curent.next = None

    return head



linked_list = LinkedList(7)
linked_list.next = LinkedList(14)
linked_list.next.next = LinkedList(21)
linked_list.next.next.next = LinkedList(14)
linked_list.next.next.next.next = LinkedList(22)
linked_list.next.next.next.next.next = LinkedList(7)

removeDuplicatesFromLinkedList(linked_list)
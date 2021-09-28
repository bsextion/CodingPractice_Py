# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	if head is None or head.next is None:
		return head
	p = reverseLinkedList(head.next)
	head.next.next = head
	head.next = None
    # Write your code here.
    return p
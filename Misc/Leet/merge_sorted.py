# Definition for singly-linked list.
#create a new empty ListNode
#check whether either list is empty, if so return the other node
#check whether l1 or l2 has the lesser value and set it to new listnode value
#increment to the next of whochever list had the least value
#create head and point to listnode

#while l1 and l2
#if l1 is less than l2, pass value into next node of new list, move to next ode
#else pass value of l2 into next node of new list, move to next node

#while l1
#pass remaining values

#while l2
#pass remaining values

#return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1


        p1 = l1
        p2 = l2
        sorted = ListNode()

        if p1.val < p2.val:
            sorted.val = p1.val
            p1 = p1.next
        else:
            sorted.val = p2.val
            p2 = p2.next

        head = sorted

        while p1 and p2:
            sorted.next = ListNode()
            sorted = sorted.next
            if p1.val < p2.val:
                sorted.val = p1.val
                p1 = p1.next
            else:
                sorted.val = p2.val
                p2 = p2.next



        while p1:
            sorted.next = ListNode()
            sorted = sorted.next
            sorted.val = p1.val
            p1 = p1.next

        while p2:
            sorted.next = ListNode()
            sorted = sorted.next
            sorted.val = p2.val
            p2 = p2.next


        return head


    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    mergeTwoLists("", l1, l2)




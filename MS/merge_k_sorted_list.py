# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        # for each pair, call a merge function
        length = len(lists)
        if length == 0: return []
        if length == 1: return lists[0]
        for i in range(0, length-1):
            result = lists[i]
            list1_copy = lists[i]
            list2_copy = lists[i+1]
            lists[i + 1] = merge(lists[i], lists[i + 1], result)
        return lists[length - 1]

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # for each

def merge(list1, list2, result):
    head_rst = None
    head_lst = list1
    head_lst2 = list2
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            result = ListNode(list1.val)
            list1 = list1.next

        else:
            result = ListNode(list2.val)
            list2 = list2.next
        result = result.next

    while list1 is not None:
        result = ListNode(list1.val)
        list1 = list1.next
        result = result.next

    while list2 is not None:
        result = ListNode(list2.val)
        list2 = list2.next
        result = result.next
    list1 = head_lst
    list2 = head_lst2
    result = head_rst
    return result

ll1 = ListNode(1)
ll1.next = ListNode(4)
ll1.next.next = ListNode(5)

ll2 = ListNode(1)
ll2.next = ListNode(3)
ll2.next.next = ListNode(4)

ll3 = ListNode(2)
ll3.next = ListNode(6)

lists = [ll1, ll2, ll3]

Solution.mergeKLists("",lists)
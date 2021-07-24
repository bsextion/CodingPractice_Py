# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        #check if either is empty, if so return
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        #create pointer
        sorted_list = ListNode(None)
        result = sorted_list

        
        #while l1 and l2
        while l1 and l2:
            #check if l1 is less than equal to l2, if so pass value to sorted_list
            if l1.val <= l2.val:
                sorted_list.val = l1.val
                l1 = l1.next
            else: 
                sorted_list.val = l2.val
                l2 = l2.next      
            sorted_list.next = ListNode(None)
            sorted_list = sorted_list.next
        
        while l1:
            sorted_list.val = l1.val
            l1 = l1.next
            sorted_list.next = l1
            sorted_list = sorted_list.next
        
        while l2:
            sorted_list.val = l2.val
            l2 = l2.next
            sorted_list.next = l2
            sorted_list = sorted_list.next
                      
        return result    
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list2 = ListNode(2)
    list2.next = ListNode(3)    
    mergeTwoLists("", list1, list2)        
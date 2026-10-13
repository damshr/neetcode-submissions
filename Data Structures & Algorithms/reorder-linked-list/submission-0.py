# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr = head
        list1 = head
        fast_ptr = head

        # find the middle
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next 
            fast_ptr = fast_ptr.next.next

        # split the list    
        list2 = slow_ptr.next
        slow_ptr.next = None
        curr = list2

        # reverse second half
        prev =  None
        curr = list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        list2 = prev

        # merge two halves
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2


        
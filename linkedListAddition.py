# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        carry = False
        current = head
        while l1 or l2 or carry:
            temp = ListNode()
            # While we are traversing the list
            if l1 and l2:
                temp.val = l1.val + l2.val + carry
                if temp.val >= 10:
                    temp.val %= 10
                    carry = True
                else:
                    carry = False
                l1 , l2 = l1.next , l2.next
            # Handle cases where only one of the lists has nodes left
            # We have no guarantee that the lists will be of the same length
            elif l1:
                temp.val = l1.val + carry
                if temp.val >= 10:
                    temp.val %= 10
                    carry = True
                else:
                    carry = False
                l1 = l1.next 
            elif l2:
                temp.val = l2.val + carry
                if temp.val >= 10:
                    temp.val %= 10
                    carry = True
                else:    
                    carry = False
                l2 = l2.next
            # In case the last addition results in a carry
            else:
                temp.val = 1
                carry = False
            current.next = temp
            current = temp
            
        return head.next
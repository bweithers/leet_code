# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next
        if len(l) <= 1: return head
        l[k-1],l[-k] = l[-k],l[k-1]
        head = l.pop(0)
        curr = head
        while l:
            curr.next = l.pop(0)
            curr = curr.next
        curr.next = None
        return head
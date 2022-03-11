# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        stack = []
        curr = head
        n = 0
        while curr:
            n+=1
            curr=curr.next
            
        k %= n
        if not k: return head
        
        curr=head
        while curr:
            if len(stack)==k+1:
                stack.pop()
            stack.insert(0,curr)
            curr = curr.next
        
        stack[-1].next=None
        stack[0].next=head
        head = stack[-2]
        
        
        
        return head
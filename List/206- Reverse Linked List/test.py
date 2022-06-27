'''
        curr = self.head
        prev = curr
        
        while curr:
            prev = curr
            curr = curr.next
        
        # currr as the dummy
        while prev:
            curr.next = prev
            prev = prev.next
'''
# x宪法先正常写的时候如果到了最后 这个prev。prev无法保障

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            # 小技巧在于这个 nxt
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
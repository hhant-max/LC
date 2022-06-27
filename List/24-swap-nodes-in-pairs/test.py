# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None: return []
        if head.next == None: return head
        
        left, right = head, head.next
        prev = None
        
        while right:
            # 第一个是特殊的因为R换过来不需要
            if prev == None:
                nxt = right.next
                left = right.next
                left.next = nxt
                head = right
            else:
                nxt = right.next
                left, right = right.next, prev.next
                left.next = nxt
            
            prev = left
            left = nxt
            right = nxt.next
        return head
        
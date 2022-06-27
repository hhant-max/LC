# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        prev, curr = dummy, head
        
        # gurantte its pair
        while curr and curr.next:
            # store pairs in advance for the handy usage
            right = curr.next
            nextLeft = curr.next.next
            
            # swap posotion
            right.next = curr
            prev.next = right 
            curr.next = nextLeft
            
            # update ptrs
            prev = curr
            curr = nextLeft
            
        return dummy.next
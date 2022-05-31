# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                # 直接找不到上一个所以你要用 prev 记录一下上一个
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next
    
        #可以把这个 curr 移到外面去
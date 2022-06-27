class Node:
	def __init__(self, val):
		self.val = val 
		self.next = None

class MyLinkedList:

	def __init__(self):
		self.head = None

	def get(self, index: int) -> int:
		if not self.head: return -1
		root = self.head
		while root and index:
			root = root.next
			index -= 1
		return root.val if root else -1 

	def addAtHead(self, val: int) -> None:
		new = Node(val, None)
		if self.head:
			new.next = self.head
			self.head = new
		else: 
            self.head = new
    
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 看这个列表存不存在？ 为啥
        if self.head:
            curr, prev = self.head, self.head
            # 在index之前
            while index and curr:
                prev = curr
                curr = curr.next
                index -= 1

            # 在index之后存在的
            new = Node(val)
            prev.next = new
            new.next = curr.next
        else:
            self.addAtHead(val)

'''		if not index:
			self.addAtHead(val)
			return None 
		if self.head:
			root = self.head
			prev = root
			while root and index:
				root, prev = root.next, root
				index -= 1
			if not index: 
				temp = prev.next 
				prev.next = Node(val,temp)
		else: 
			if not index: self.addAtHead(val)
'''


    def deleteAtIndex(self, index: int) -> None:
        		if self.head:
			if not index: 
				self.head = self.head.next
				return None
			root = self.head
			prev = root
			while root and index:
				root, prev = root.next, root
				index -= 1
			if not index: 
				if root: prev.next = root.next
				else: prev.next = root
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
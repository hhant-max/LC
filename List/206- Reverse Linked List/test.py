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


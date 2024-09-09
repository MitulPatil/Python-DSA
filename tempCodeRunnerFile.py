if current.data==data:
                self.head=current.next.next
                current.next.prev=None
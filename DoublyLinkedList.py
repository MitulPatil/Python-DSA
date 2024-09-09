class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class DLL:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        return self.head==None
        
    def insert_at_start(self,data):
        new_node=Node(None,data,self.head)
        if not self.is_empty(): 
            self.head.prev=new_node
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(None,data)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            new_node.prev=current.next

    def insert_after(self,current,data):
        if current is not None:
            new_node=Node(current,data,current.next)
            if current.next is not None:
                current.next.prev=new_node
            current.next=new_node

    def search(self,data):
        current=self.head
        while current is not None:
            if current.data==data:
                return current
            current=current.next
        return None            

    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next

    def delete_first(self):
        if self.head is not None:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None
    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:    
            current=self.head
            while current.next.next is not None:
                current=current.next
            current.next=None
    def delete_data(self,data):
        if self.head is None:
            pass
        else:
            current=self.head
            while current is not None:
                if current.next is not None:
                    current.next.prev=current.prev
                if current.prev is not None:
                        current.prev.next=current.next
                else:
                    self.head=current.next
                break
            current=current.next        
                
    def __iter__(self):
        return DLLIterator(self.head)                                    

class DLLIterator:
    def __init__(self,head):
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data    

list=DLL()

list.insert_at_start(40)
list.insert_at_start(30)
list.insert_at_start(20)
list.insert_at_start(10)
list.insert_at_end(50)
list.print_list()
print()
list.insert_after(list.search(30),60)
list.print_list()
list.delete_first()
print()
list.print_list()
list.delete_last()
print()
list.print_list()
print()
list.delete_data(20)
list.print_list( )
print()
for data in list:
    print(data,end=' ')
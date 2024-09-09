# Node class to create Linked list Node
class Node:      
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

# Single Linked List class contains all operation on linked list
class SSL:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return self.head==None  
      
    def insert_at_start(self,data):
        new_node=Node(data,self.head)
        self.head=new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.is_empty():
            current=self.head
            while current.next is not None:
                current=current.next
            current.next = new_node 
        else: 
            self.head=new_node

    def insert_after(self,current,data):
        if current is not None:
            new_node=Node(data,current.next)
            current.next=new_node

    def insert_at_position(self,pos,data):
        new_node=Node(data)
        current=self.head
        num=1
        while current is not None:
            if num == pos-1:
                new_node.next=current.next
                current.next=new_node
            current=current.next
            num+=1         

    def search(self,data):
        current=self.head
        while current.next is not None:
            if current.data==data:
                return current
            current=current.next
        return None    

    def print_list(self):
        current= self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next

    def delete_first(self):
        if self.head is not None:
            self.head=self.head.next   
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
        elif self.head.next is None:
            if self.head.data == data:
                self.head=None
        else:
            current=self.head
            if current.data == data:
                self.head=current.next
            else:
                while current.next is not None:
                    if current.next.data == data:
                        current.next=current.next.next
                        break
                    current=current.next
    def __iter__(self):
        return SSLIterator(self.head)
                    
# to make list iterable
class SSLIterator:
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

Mylist = SSL()
Mylist.insert_at_start(10)
Mylist.insert_at_end(20)              
Mylist.insert_at_end(40)              
Mylist.insert_at_end(50)              

Mylist.print_list()
print()    
Mylist.insert_after(Mylist.search(40),70)
Mylist.print_list()
print()

print(Mylist.search(50)) 

Mylist.delete_first()
Mylist.print_list()
print()

Mylist.delete_last()
Mylist.print_list()
print()

Mylist.delete_data(40)
Mylist.print_list() 
print() 

for data in Mylist:
    print(data,end=" ")

print()
Mylist.insert_at_position(3,80)
Mylist.print_list()
print()
Mylist.insert_at_position(5,90)
Mylist.print_list()
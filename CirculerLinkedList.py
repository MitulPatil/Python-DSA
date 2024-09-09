class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class CLL:
    def __init__(self,tail=None):
        self.tail=tail
    def is_empty(self):
        return self.tail==None
    
    def insert_at_first(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.tail=new_node
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.tail=new_node
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
            self.tail=new_node
    def insert_after(self,current,data):
        if current is not None:
            new_node=Node(data,current.next)
            current=new_node
            if current==self.tail:
                self.tail=new_node           

    def search(self,data):
        if self.is_empty():
            return None
        current=self.tail.next
        while current != self.tail:
            if current.data==data:
                return data
            current=current.next
        if current.data==data:
            return data
        return None
    
    def print_CLL(self):
        if not self.is_empty():
            current=self.tail
            while current != self.tail:
                print(current.data,end=' ')
                current=current.next
            print(current.data)    
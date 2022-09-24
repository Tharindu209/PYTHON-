# create node class
class Node():
    # variable initializing(coonstructure)
    def __init__(self,value):
        self.value = value
        self.next = None
    
    # deconstructure
    def __repr__(self):
        return f'{self.value}'

# create link list class
class Linkedlist():
    # variable initializing(coonstructure)
    def __init__(self):
        # head
        self.head = None
        # add counter
        self.count = 0
        
    # check this list is empty?
    def is_empty(self):
        return self.head  == None
    
    # append values 
    def add(self,data):
        # create node
        new_node = Node(data)
        self.count += 1
        # append new node address to the head 
        new_node.next = self.head
        self.head = new_node
    
    # deconstructure
    def __repr__(self):
        printdata = self.head
        print("list is: ", end = "")
        while (printdata):
            print(printdata,end = '->')
            printdata = printdata.next  
        
        return f'\ncount: {self.count}'
    
    
    def insert(self,value,index):
        if index == 0:
            self.add(value)
            return
        if index > self.count:
            raise IndexError('out of range')
        new = Node(value)
        current = self.head
            
        while index > 1:
            current = current.next
            index -=1
            
        next_1 = current.next
            
        current.next = new
        new.next = next_1
        
        self.count += 1

    def remove(self,index):
        if index >= self.count:
            raise IndexError('out of range') 

        current = self.head
        while index < 1:
            current = current.next
            index -= 1
        
        previous = current
        current = current.next
        n_next = current.next

        previous.next = n_next
        current = None
        self.count -= 1
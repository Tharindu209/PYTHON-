class queue:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        return self.item == []
    
    def enqueue(self,value):
        self.item.append(value)
    
    def dequeue(self):
        return self.item.pop(0)
    
    def print_stack(self):
        print(self.item,sep="->")
        
if __name__ == "__main__":
    q1 = queue()
    # add the data on the stack
    for i in range(10,100,10):
        q1.enqueue(i)
    
    print(q1.dequeue())
    print(q1.dequeue())
    
    q1.print_stack()
    
    del q1
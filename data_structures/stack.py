class stack:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        return self.item == []
    
    def push(self,value):
        self.item.insert(0,value)
    
    def pop(self):
        return self.item.pop(0)
    
    def print_stack(self):
        print(self.item,sep="->")
        
if __name__ == "__main__":
    s1 = stack()
    # add the data on the stack
    for i in range(10,100,10):
        s1.push(i)
    
    print(s1.pop())
    print(s1.pop())
    
    s1.print_stack()
    
    del s1
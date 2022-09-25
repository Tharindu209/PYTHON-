class graph:
    def __init__(self,size):
        self.adj = [ [0]*size for i in range(size) ]
        self.size = size
        
    def add_edge(self, x,y):
        if (x >self.size) or (y > self.size) or (x < 0) or (y < 0):
            print("Invalid Edge")
        else:
            self.adj[x-1][y-1] = 1
            self.adj[x-1][y-1] = 1
            
    def remove_edge(self, x, y):
        if (x >self.size) or (y
        >self.size) or (x < 0) or (y
        < 0):
            print("Invalid Edge")
        else:
            self.adj[x-1][y
            -1] = 0
            self.adj[y
            -1][x-1] = 0
    
    def display(self):
        for row in self.adj:
            for val in row:
                print('{:4}'. format(val), end=" ")
            print()
            
if __name__ == "__main__":
    g = graph(5)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 5)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    
    g.display()
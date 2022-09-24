from collections import defaultdict
from doctest import DONT_ACCEPT_TRUE_FOR_1

class graph:
    def __init__(self):
        self.adj = defaultdict(list)
        
    def addEdge(self,u,v):
        if not u in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
    
    def print(self):
        return self.adj
    
def bfs(g,start,n):
    visit = []
    visited = [False] * (n)
    queue = []
    
    queue.append(start)
    visited[start] = True
    
    while queue:
        s = queue.pop(0)
        visit.append(s)
        
        for n in g.adj[s]:
            if visited[n] == False:
                queue.append(n)
                visited[n] = True
    
    return visit

def allEdgescount(edges):
    result = set()
    for i in edges:
        for j in i:
            result.add(j)
            
    return len(result)
                
        
if __name__ == "__main__":
    g = graph()
    edges = [(0, 1),(2, 3),(3, 1),(1, 2),(0, 3),(4, 2),(5, 5),(4, 5)]
    for i,j in edges:
        g.addEdge(i,j)
    print(g.print())
    print(bfs(g,4,allEdgescount(edges)))
    del g
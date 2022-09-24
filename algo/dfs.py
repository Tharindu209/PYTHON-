from collections import defaultdict
from dis import dis
from doctest import DONT_ACCEPT_TRUE_FOR_1
from itertools import count

class graph:
    def __init__(self):
        self.adj = defaultdict(list)
        
    def addEdge(self,u,v):
        if not u in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
    
    def print(self):
        return self.adj
    
def DFS_visit(g,v,discovered):
    for i in g.adj[v]:
        if not discovered[i]:
            discovered[i] = True
            visit.append(i)
            DFS_visit(g,i,discovered)
            
def DFS(adj,minimum,maximum,discovered):
    
    for i in range(minimum,maximum):
        if not discovered[i]:
            discovered[i] = True
            visit.append(i)
            DFS_visit(adj,i,discovered)
            
def allEdges(edges):
    result = set()
    for i in edges:
        for j in i:
            result.add(j)
            
    return result
    
if __name__ == "__main__":
    g = graph()
    edges = [(0, 1),(2, 3),(3, 1),(1, 2),(0, 3),(4, 2),(5, 5),(4, 5)]
    for i,j in edges:
        g.addEdge(i,j)
    print(g.print())
    
    visit = []
    edge_set = allEdges(edges)
    n  = len(edge_set)+min(edge_set)
    discovered = [False] * (n)
    DFS(g,min(edge_set),n,discovered)
    
    
    print(visit)
    del g
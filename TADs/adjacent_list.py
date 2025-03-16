#Lista de adjacencias para representar o Grafo

class AdjacentList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}
    
    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
    
    def get_neighbor(self, v):
        return self.adj_list.get(v, [])  

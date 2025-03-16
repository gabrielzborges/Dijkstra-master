# A sua tarefa ser ́a entender e implementar, de forma modularizada e eficiente, os caminhos de custo m ́ınimo entre
# todos os pontos de transporte da rede. Para isso, vocˆe dever ́a seguir os seguintes passos:
# 1. Sua entrada ser ́a o n  ́o de origem Vsrc ao qual deseja-se calcular os caminhos de custo m ́ınimo e o grafo
# G(V,(E,ω) = d1,...,n−1 - representado pelas distˆancias entre os n  ́os Vi e todos os demais n −1 n  ́os da
# rede) ∴G(V,d1,...,n−1), com V representando o conjunto de v ́ertices da rede de postos de transporte;
# 2. Utilize o algoritmo de Dijkstra para calcular os caminhos m ́ınimos de todos os n  ́os em V do n  ́o Vsrc para
# todos os demais n  ́os.
# 3. Para cada par a,b com a sendo o ponto de partida e b sendo um potencial destino, o caminho de custo
# m ́ınimo de ser explicitado (mostrado, com todos os n  ́os intermedi ́arios do caminho total), bem como o valor
# de seu custo de transporte

#Deve-se implementar criando dois TAD, sendo um deles uma heap

from TADs.heap_min import HeapMin
from TADs.adjacent_list import AdjacentList

def dijkstra(graph, origin):
    heap = HeapMin()
    heap.insert(origin, 0)
    
    vertices = graph.vertices
    distancia = {v: float('inf') for v in range(vertices)}
    antecessor = {v: None for v in range(vertices)}

    distancia[origin] = 0

    while not heap.is_empty():
        u_node, u_weight = heap.remove_min()
        for v_node, edge_weight in graph.get_neighbor(u_node):
            new_weight = u_weight + edge_weight

            if new_weight < distancia[v_node] and v_node != origin:
                distancia[v_node] = new_weight
                antecessor[v_node] = u_node

                if v_node in heap.pos:
                    heap.update_lower_priority(v_node, new_weight)
                else:
                    heap.insert(v_node, new_weight)
    
    return distancia, antecessor
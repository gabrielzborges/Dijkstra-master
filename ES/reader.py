from TADs.adjacent_list import AdjacentList

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    origin = int(lines[0].strip().split('_')[1])  # node origem
    vertices = len(lines) - 1  # numero de vertices
    graph = AdjacentList(vertices)

    for _, line in enumerate(lines[1:]):
        data_to_others_vertex = line.strip().split(', ')
        node_index = int(data_to_others_vertex[0].split('_')[1])  # vertice atual (da linha)

        for j, weight in enumerate(data_to_others_vertex[1:]):  
            if weight == "bomba": #Tratar como uma aresta inexistente
                weight = float('inf')
            else:
                weight = float(weight)
            node_destino = j if j < node_index else j + 1  # ajusta indice lido na linha

            if weight > 0:  #ignora os vertices que nao tem arestas a partir do node_index
                graph.add_edge(node_index, node_destino, weight)  
    
    return origin, graph
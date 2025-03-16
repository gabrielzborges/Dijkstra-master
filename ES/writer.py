def build_path(antecessor, destino, origem):
    path = []
    actual = destino
    
    while actual is not None:
        path.append(f"node_{actual}")
        actual = antecessor[actual]

    #if abaixo eh para atender o que se espera da saida ter o node_origem <- node_origem
    if len(path) == 1 and path[0] == f"node_{origem}":
        path.append(f"node_{origem}")
    
    return " <- ".join(path)

def write_file(filename, distancia, antecessor, origem):
    with open(filename, 'w') as file:
        for destino in sorted(distancia, key=lambda  v: distancia[v]):
            path = build_path(antecessor, destino, origem)
            file.write(f"SHORTEST PATH TO node_{destino}: {path} (Distance: {distancia[destino]:.2f})\n")
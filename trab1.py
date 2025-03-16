import sys
import time
import statistics

N_REPETICOES = 20

from dijkstra import dijkstra
from ES.reader import read_file
from ES.writer import write_file


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Uso: python trab1 <arquivo_entrada> <arquivo_saida> [--stats]")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    executar_stats = len(sys.argv) == 4 and sys.argv[3] == "--stats"

    origem, grafo = read_file(arquivo_entrada)

    if executar_stats:
        print(f"Executando {N_REPETICOES} medições para {arquivo_entrada}...")
        tempos = []
        
        for _ in range(N_REPETICOES):
            t_inicial = time.time()
            dist, antecessor = dijkstra(grafo, origem)
            t_final = time.time()
            tempos.append(t_final - t_inicial)

        write_file(arquivo_saida, dist, antecessor, origem)

        media_tempo = statistics.mean(tempos)
        desvio_tempo = statistics.stdev(tempos) if N_REPETICOES > 1 else 0

        print(f"Tempo médio de execução: {media_tempo:.6f} segundos")
        print(f"Desvio padrão: {desvio_tempo:.6f} segundos")

        for tempo in tempos:
            print(f"""Execução {tempos.index(tempo) + 1}: Tempo: {tempo:.6f} segundos""")
    else:
        dist, antecessor = dijkstra(grafo, origem)
        write_file(arquivo_saida, dist, antecessor, origem)

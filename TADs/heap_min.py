# Estrutura HeapMin para obter o nó de menor custo rapidamente

class HeapMin:
    def __init__(self):
        self.heap = [] #vai armazer tupla (prioridade, nó)
        self.pos = {} #vai armazenar a posição de cada nó
    
    # funcao auxiliar para troca de posicao dos nós em i e j
    def _swap(self, i, j):
        self.pos[self.heap[i][1]] = j
        self.pos[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # funcao auxiliar para corrigir a heap subindo elemento
    def _move_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2
    
    # funcao auxiliar para corrigir a heap descendo elemento
    def _move_down(self, index):
        length = len(self.heap)

        while True:
            left = 2 * index + 1    # achando elemento que graficamente seria a esquerda
            right = 2 * index + 2   # achando elemento que graficamente seria a direita
            small = index

            # os ifs abaixo verificam se o elemento da esquerda ou direita é menor que o elemento atual
            if left < length and self.heap[left][0] < self.heap[small][0]:
                small = left
            
            if right < length and self.heap[right][0] < self.heap[small][0]:
                small = right

            # caso o menor não seja o elemento atual, entao troca
            if small != index:
                self._swap(index, small)
                index = small
            else:
                break
    
    # funcao que verifica se a heap está vazia
    def is_empty(self):
        return len(self.heap) == 0
    
    # funcao insere um nó com prioridade na heap
    def insert(self, node, priority):
        self.heap.append((priority, node))
        node_index = len(self.heap) - 1
        self.pos[node] = node_index
        self._move_up(node_index)
    
    # funcao remove e retorna o nó de menor prioridade
    # retorna o nó e a prioridade
    def remove_min(self):
        if not self.heap:
            return None, None

        self._swap(0, len(self.heap) - 1)
        priority, node = self.heap.pop()
        del self.pos[node]

        if self.heap:
            self._move_down(0)
        
        return node, priority

    # funcao que atualiza a prioridade de um nó se ela for menor
    def update_lower_priority(self, node, new_priority):
        if node in self.pos:
            index = self.pos[node]

            if self.heap[index][0] > new_priority:
                self.heap[index] = (new_priority, node)
                self._move_up(index)
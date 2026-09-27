from collections import deque
from auxiliares import get_goal, neighbors,_rebuild_path

def bfs_path(start, grid):
    if grid[start[0]][start[1]] == 2:
        return [start]

    visitados = {start}         
    cola = deque([start])        # Cola deque para aplicar FIFO
    came_from = {start: None}    

    while cola:
        nodo_actual = cola.popleft()

        if grid[nodo_actual[0]][nodo_actual[1]] == 2:
            return _rebuild_path(came_from, nodo_actual)

        # Iteramos sobre nodos vecinos
        for adyacente in neighbors(nodo_actual, grid):
            # Si no se ha visitado
            if adyacente not in visitados:
                visitados.add(adyacente)
                came_from[adyacente] = nodo_actual
                cola.append(adyacente)

    return None

def dfs_path(start, grid):
    if grid[start[0]][start[1]] == 2:
        return [start]

    visitados = set()            
    pila = [start]               # Pila para aplicar LIFO
    came_from = {start: None}    

    while pila:                  # Mientras la pila no este vacia
        nodo_actual = pila.pop()  
        if grid[nodo_actual[0]][nodo_actual[1]] == 2:
            return _rebuild_path(came_from, nodo_actual)

        if nodo_actual not in visitados: 
            visitados.add(nodo_actual)

            # Agregamos los vecinos a la pila
            for adyacente in neighbors(nodo_actual, grid):
                # Si el nodo adyacente no se ha visitado
                if adyacente not in visitados and adyacente not in came_from:
                    # Apilar el nodo
                    came_from[adyacente] = nodo_actual
                    pila.append(adyacente)

    return None
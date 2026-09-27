from collections import deque

#Algoritmo de busqueda en anchura aplicado para grafos con matriz de adyacencia
def bfs_matriz(matriz, nodo_inicio):
    
    
    visitados = {nodo_inicio}       # Conjunto de nodos visitados
    cola = deque([nodo_inicio])      # Cola deque para aplicar FIFO
    orden_visita = []               # Lista para almacenar nodos visitados 

    while cola:
        nodo_actual = cola.popleft()
        orden_visita.append(nodo_actual)

        # Iteramos sobre todos los posibles nodos adyacentes en la matriz
        for adyacente in range(len(matriz)):
            # Si hay conexión y no se a visitado
            if matriz[nodo_actual][adyacente] == 1 and adyacente not in visitados:
                visitados.add(adyacente)
                cola.append(adyacente)

    return orden_visita



# Algoritmo de busqueda en profundidad para grafos con matriz de adyacencia
def dfs(matriz, nodo_inicio):
    visitados = set() #Nodos visitados
    pila = [nodo_inicio]  # Estructura LIFO 
    orden_visita = [] # Orden de los nodos

    while pila: # Mientras la pila no este vacia
        nodo_actual = pila.pop()  

        if nodo_actual not in visitados: 
            visitados.add(nodo_actual)
            orden_visita.append(nodo_actual)

            # Agregamos los vecinos a la pila
            for adyacente in range(len(matriz) - 1, -1, -1):
                # Si existe una arista  y el nodo adyacente no se ha visitado
                if matriz[nodo_actual][adyacente] == 1 and adyacente not in visitados:
                    # Apilar el nodo
                    pila.append(adyacente)

    return orden_visita
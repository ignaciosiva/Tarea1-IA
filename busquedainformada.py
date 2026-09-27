
import heapq

# heuristica utilizada para determinar la distancia entre dos puntos de una trayectoria en forma de cuadrícula

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
# Funcion que devuelve el camino a la meta
def _rebuild_path(came_from, current):
    
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
# Funcion que encuentra los posibles vecinos
def neighbors(current, grid):

    r, c = current
    potential_neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]# ve los 4 posibles vecinos
    valid = []
    max_rows = len(grid)
    max_cols = len(grid[0])
    
    for x, y in potential_neighbors:
        if 0 <= x < max_rows and 0 <= y < max_cols:
            cell_value = grid[x][y]
            # Puede avanzar si es camino  o salida 
            if cell_value in (1, 2):
                valid.append((x, y))
                
    return valid

def greedy_best_first_path(start, grid):
    if grid[start[0]][start[1]] == 2:
        return [start]
        
    counter = 0
    goal = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                goal = (r, c)
                break
         
    frontier = [(manhattan(start, goal), counter, start)] # lista ordenada segun la menor distancia via heuristica manhattan 
    came_from = {start: None} #Diccionario que guarda el camino recorrido 
    visited = {start}
    
    while frontier:
        _, _, current = heapq.heappop(frontier)
        
        
        if grid[current[0]][current[1]] == 2:
            return _rebuild_path(came_from, current)
        # Si no se a llegado a la meta, seguimos recorriendo en los vecinos    
        for nxt in neighbors(current, grid):
            if nxt not in visited:
                visited.add(nxt)
                came_from[nxt] = current
                counter += 1
                heapq.heappush(frontier, (manhattan(nxt, goal), counter, nxt))
                
    return None
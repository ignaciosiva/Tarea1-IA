
import heapq
from auxiliares import neighbors, _rebuild_path, get_goal

# heuristica utilizada para determinar la distancia entre dos puntos de una trayectoria en forma de cuadrícula

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

COSTOS_AGENTES = {}


def greedy_best_first_path(start, grid):
    if grid[start[0]][start[1]] == 2:
        return [start]
        
    counter = 0
    goal = get_goal(grid)
         
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

def a_star_path(start, grid):
    
    if grid[start[0]][start[1]] == 2:
        return [start]
        
    goal = get_goal(grid)
        
    counter = 0
    start_h = manhattan(start, goal)
    frontier = [(start_h, counter, start)]
    
    came_from = {start: None}
    cost = {start: 0}  #costo acumulado
    
    while frontier:
        _, _, current = heapq.heappop(frontier)
        
        if grid[current[0]][current[1]] == 2:
            return _rebuild_path(came_from, current)
            
        for nxt in neighbors(current, grid):
            nr, nc = nxt
            
            if grid[nr][nc] == 2:
                costo_transito = 1.0
            else:
                costo_transito = COSTOS_AGENTES.get(nxt, 1.0)
                
            new_cost = cost[current] + costo_transito
            
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                counter += 1
                f_score = new_cost + manhattan(nxt, goal)
                heapq.heappush(frontier, (f_score, counter, nxt))
                came_from[nxt] = current
                
    return None
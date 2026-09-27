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


def get_goal(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                return (r, c)
    return None
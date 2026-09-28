import random
from auxiliares import neighbors, get_goal
from busquedainformada import manhattan

def genetic_path(start, grid):
    if grid[start[0]][start[1]] == 2:
        return [start]
        
    goal = get_goal(grid)
    
    # Parámetros 
    GENERACIONES = 30
    POBLACION = 20
    MAX_PASOS = 60  
    
    # Función auxiliar para generar un camino aleatorio válido desde el inicio
    def generar_individuo():
        camino = [start]
        actual = start
        for _ in range(MAX_PASOS):
            if grid[actual[0]][actual[1]] == 2:
                break
            vecinos = neighbors(actual, grid)
            if not vecinos:
                break
            if len(camino) > 1:
                nodo_anterior = camino[-2]  
                vecinos_filtrados = []
                for v in vecinos:
                    if v != nodo_anterior:
                        vecinos_filtrados.append(v)
            else:
                vecinos_filtrados = vecinos

            if vecinos_filtrados:
                siguiente = random.choice(vecinos_filtrados)
            else:
                siguiente = random.choice(vecinos)
            
            camino.append(siguiente)
            actual = siguiente
            if grid[actual[0]][actual[1]] == 2:
                break
        return camino

    def evaluar_fitness(camino):
        ultimo_paso = camino[-1]
        
        distancia_meta = manhattan(ultimo_paso, goal)
        
        if grid[ultimo_paso[0]][ultimo_paso[1]] == 2:
            penalizacion_meta = 0
        else:
            penalizacion_meta = 100  
        
        penalizacion_longitud = len(camino) * 0.2
        
        return distancia_meta + penalizacion_meta + penalizacion_longitud

    # poblacion inicial
    poblacion = [generar_individuo() for i in range(POBLACION)]
    
    mejor_camino_global = None
    mejor_fitness_global = float('inf')

    for i in range(GENERACIONES):
        # ordenar poblacion por aptitud
        poblacion.sort(key=evaluar_fitness)
        
        # Guardar el mejor individuo de esta generación
        actual_mejor = poblacion[0]
        actual_fitness = evaluar_fitness(actual_mejor)
        
        if actual_fitness < mejor_fitness_global:
            mejor_fitness_global = actual_fitness
            mejor_camino_global = actual_mejor
            
        if grid[mejor_camino_global[-1][0]][mejor_camino_global[-1][1]] == 2:
            break
            
        #Nos quedamos con la mitad superior 
        padres = poblacion[:POBLACION // 2]
        nueva_poblacion = list(padres)
        
        while len(nueva_poblacion) < POBLACION:
            padre1 = random.choice(padres)
            padre2 = random.choice(padres)
            # reproduccion
            comunes = []
            for n in padre1[1:]:  
                if n in padre2:
                    comunes.append(n)
            
            if comunes:
                punto_cruce = random.choice(comunes)
                idx1 = padre1.index(punto_cruce)
                idx2 = padre2.index(punto_cruce)
                hijo = padre1[:idx1] + padre2[idx2:]
            else:
                hijo = list(padre1)  # Si no hay intersección común, heredamos al padre 1
                
            # Mutación 
            if len(hijo) < 3 and grid[hijo[-1][0]][hijo[-1][1]] != 2:
                hijo = generar_individuo()
                
            nueva_poblacion.append(hijo)
            
        poblacion = nueva_poblacion

    # Crea un camino limpio sin bucles a traves del camino global
    if mejor_camino_global:
        camino_limpio = []
        for nodo in mejor_camino_global:
            if nodo in camino_limpio:
                # Si pasa por un nodo ya presente, recortamos el bucle intermedio
                idx = camino_limpio.index(nodo)
                camino_limpio = camino_limpio[:idx+1]
            else:
                camino_limpio.append(nodo)
        return camino_limpio

    return None
import busquedainformada
class simulador:
    def __init__(self, grid, start, number_people, k_turns):
        
        self.grid = [fila[:] for fila in grid]
        # Creamos una lista donde todos los agentes comparten la misma celda al inicio
        self.agentes = [start for _ in range(number_people)]
        self.k = k_turns
        self.turno_actual = 0
        self.sobrevivientes = []
        self.bajas = []

    def propagar_fuego(self):
        
        propagar = []
        max_rows = len(self.grid)
        max_cols = len(self.grid[0])
        
        for r in range(max_rows):
            for c in range(max_cols):
                if self.grid[r][c] == 3:
                    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                        if 0 <= nr < max_rows and 0 <= nc < max_cols:
                            if self.grid[nr][nc] == 1:
                                propagar.append((nr, nc))
                                
        for r, c in propagar:
            self.grid[r][c] = 3

    

    def ejecutar_turno(self, algoritmo):
        self.turno_actual += 1
        
        if self.turno_actual % self.k == 0:
            self.propagar_fuego()
            
        busquedainformada.COSTOS_AGENTES.clear()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 1:
                    num_agentes = self.agentes.count((r, c))
                    if num_agentes > 0:
                        busquedainformada.COSTOS_AGENTES[(r, c)] = (num_agentes / 2.0) + 1.0

        activos = []
        destinos_ocupados = {}
        
        for agente in self.agentes:
            r, c = agente
            
            if self.grid[r][c] == 3:
                self.bajas.append(agente)
                continue
                
            camino = algoritmo(agente, self.grid)
            
            if camino and len(camino) > 1:
                siguiente_paso = camino[1]
                nr, nc = siguiente_paso
                
                if self.grid[nr][nc] == 3:
                    self.bajas.append(agente)  # Murio
                elif self.grid[nr][nc] == 2:
                    self.sobrevivientes.append(siguiente_paso)  # EScapo
                else:
                    
                    agentes_celda = self.agentes.count(siguiente_paso)
                    agentes_transitorios = destinos_ocupados.get(siguiente_paso, 0)
                    total_proyectado = agentes_celda + agentes_transitorios
                    
                    if total_proyectado >= 40:  
                        activos.append(agente)
                    else:
                        # Si hay espacio, registramos que este agente ocupará la celda y avanzamos
                        destinos_ocupados[siguiente_paso] = agentes_transitorios + 1
                        activos.append(siguiente_paso)
            else:
                # Espera
                activos.append(agente)
                
        self.agentes = activos
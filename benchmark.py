import statistics
from simulador import simulador

def ejecutar_benchmarking_oficial(algoritmo, grid, start, number_people, k_turns, iteraciones):
    # Debemos registrar la tase de supervivencia y el turno de salida del ultimo superviviente para las estadisticas
    tasas_supervivencia = []
    turnos_ultimos_sobrevivientes = []
    
    
    for i in range(iteraciones):
        sim = simulador(grid, start, number_people, k_turns)
        turnos_salida_sobrevivientes = []

        while sim.agentes:
            prev_sobrevivientes_count = len(sim.sobrevivientes)
            
            sim.ejecutar_turno(algoritmo)
            
            # Si hay nuevos sobrevivientes añadimos su turno de salida 
            nuevos_salidos = len(sim.sobrevivientes) - prev_sobrevivientes_count
            for _ in range(nuevos_salidos):
                turnos_salida_sobrevivientes.append(sim.turno_actual)
                
        # Calculamos tasa de supervivencia
        n_sobrevivientes = len(sim.sobrevivientes)
        tasa_supervivencia = (n_sobrevivientes / number_people) * 100
        tasas_supervivencia.append(tasa_supervivencia)
        
        if turnos_salida_sobrevivientes:
        
            ultimo_turno_sobreviviente = turnos_salida_sobrevivientes[-1]
            turnos_ultimos_sobrevivientes.append(ultimo_turno_sobreviviente)
        else:
            turnos_ultimos_sobrevivientes.append(0)
    # Omitimos tiempos 0, osea que no hayan sobrevivientes 
    tiempos_validos = [t for t in turnos_ultimos_sobrevivientes if t > 0]
    
    if tiempos_validos:
        media_turnos = round(statistics.mean(tiempos_validos), 2)
        desv_turnos = round(statistics.stdev(tiempos_validos), 2) if len(tiempos_validos) > 1 else 0
        min_turnos = min(tiempos_validos)
        max_turnos = max(tiempos_validos)
    else:
        media_turnos = desv_turnos = min_turnos = max_turnos = 0

    resumen = {
        "Tasa de Supervivencia Promedio": f"{statistics.mean(tasas_supervivencia):.2f}%",
        "Media de Turnos (Último Sobreviviente)": media_turnos,
        "Desviación Estándar Turnos": desv_turnos,
        "Mínimo de Turnos": min_turnos,
        "Máximo de Turnos": max_turnos,
        "Iteraciones Totales": iteraciones
    }
    
    return resumen
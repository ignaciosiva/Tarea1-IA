import statistics
from simulador import simulador
 
MAX_TURNOS = 1000  
 
 
def ejecutar_benchmarking_oficial(algoritmo, grid, start, number_people, k_turns, iteraciones):
    tasas_supervivencia = []
    turnos_salida = []  
 
    for i in range(iteraciones):
        sim = simulador(grid, start, number_people, k_turns)
 
        while sim.agentes and sim.turno_actual < MAX_TURNOS:
            prev = len(sim.sobrevivientes)
            sim.ejecutar_turno(algoritmo)
 
            # Registramos el turno de salida de cada nuevo sobreviviente
            for _ in range(len(sim.sobrevivientes) - prev):
                turnos_salida.append(sim.turno_actual)
 
        tasas_supervivencia.append(len(sim.sobrevivientes) / number_people * 100)

 
    if turnos_salida:
        media = round(statistics.mean(turnos_salida), 2)
        if len(turnos_salida) > 1:
            desv = round(statistics.stdev(turnos_salida), 2)
        else:
            desv = 0
        minimo = turnos_salida[0]
        maximo = turnos_salida[-1]
    else:
        media = desv = minimo = maximo = 0
 
    return {
        "Tasa de Supervivencia Promedio": f"{statistics.mean(tasas_supervivencia):.2f}%",
        "Media de Turnos": media,
        "Desviación Estándar Turnos": desv,
        "Mínimo de Turnos (Primer Sobreviviente)": minimo,
        "Máximo de Turnos (Último Sobreviviente)": maximo,
        "Iteraciones Totales": iteraciones,
    }


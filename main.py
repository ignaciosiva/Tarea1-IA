
from simulador import simulador 
from benchmark import ejecutar_benchmarking_oficial
from busquedainformada import a_star_path, greedy_best_first_path
from busquedanoinformada import bfs_path, dfs_path



if __name__ == "__main__":
    mapa_prueba = [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [4, 1, 4, 4, 4, 4, 4, 4, 1, 4],
        [4, 1, 4, 3, 1, 1, 1, 4, 1, 4], 
        [4, 1, 4, 1, 4, 4, 1, 4, 1, 4],
        [4, 1, 1, 1, 1, 1, 1, 1, 2, 4], 
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    ]

    punto_inicio = (1, 1)  
    cantidad_personas = 200
    k_fuego = 3           

    
    algoritmos = {
        "A*": a_star_path,
        "Greedy Best-First": greedy_best_first_path,
        "BFS": bfs_path,
        "DFS": dfs_path,
    }

    print("="*50)
    print(" Inicio")
    print("="*50)

    for nombre, func in algoritmos.items():
        print(f"\n[Ejecutando] -> {nombre} (200 iteraciones)...")
        resultados = ejecutar_benchmarking_oficial(
            algoritmo=func,
            grid=mapa_prueba,
            start=punto_inicio,
            number_people=cantidad_personas,
            k_turns=k_fuego,
            iteraciones=200
        )
        
        for metrica, valor in resultados.items():
            print(f"   - {metrica}: {valor}")

    print("\n" + "="*50)
    print("Termino")
    print("="*50)
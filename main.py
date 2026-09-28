from benchmark import ejecutar_benchmarking_oficial
from busquedainformada import a_star_path, greedy_best_first_path
from busquedanoinformada import bfs_path, dfs_path
from genetico import genetic_path
from mapas import MAPAS
 
 
if __name__ == "__main__":
    cantidad_personas = 100
    k_fuego = 3
    ITERACIONES = 80   
 
    algoritmos = {
        "A*": a_star_path,
        "Greedy Best-First": greedy_best_first_path,
        "BFS": bfs_path,
        "DFS": dfs_path,
        "Genetico": genetic_path
    }
 
    print("=" * 50)
    print(" Inicio")
    print("=" * 50)
 
    for nombre_mapa, (grilla, punto_inicio) in MAPAS.items():
        print("\n" + "#" * 50)
        print(f" {nombre_mapa}")
        print("#" * 50)
 
        for nombre, func in algoritmos.items():
            print(f"\n[Ejecutando] -> {nombre} ({ITERACIONES} iteraciones)...")
            resultados = ejecutar_benchmarking_oficial(
                algoritmo=func,
                grid=grilla,
                start=punto_inicio,
                number_people=cantidad_personas,
                k_turns=k_fuego,
                iteraciones=ITERACIONES
            )
 
            for metrica, valor in resultados.items():
                print(f"   - {metrica}: {valor}")
 
    print("\n" + "=" * 50)
    print("Termino")
    print("=" * 50)

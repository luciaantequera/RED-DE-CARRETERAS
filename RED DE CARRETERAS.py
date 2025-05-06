import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

# ===== 1. CREAR LA RED DE CIUDADES =====
def crear_grafo(ciudades, distancia_max=100):
    G = nx.complete_graph(len(ciudades))
    mapping = dict(zip(range(len(ciudades)), ciudades))
    G = nx.relabel_nodes(G, mapping)

    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(10, distancia_max)
    
    return G

# ===== 2. NEAREST NEIGHBOR (ALGORITMO VORAZ) =====
def nearest_neighbor(G, inicio):
    visitadas = [inicio]
    actual = inicio
    total = 0

    while len(visitadas) < len(G.nodes):
        vecinos = [(vecino, G[actual][vecino]['weight']) 
                   for vecino in G.neighbors(actual) if vecino not in visitadas]
        siguiente, peso = min(vecinos, key=lambda x: x[1])
        visitadas.append(siguiente)
        total += peso
        actual = siguiente

    total += G[actual][inicio]['weight']  # Volver al inicio
    visitadas.append(inicio)
    return visitadas, total

# ===== 3. BACKTRACKING (TSP EXACTO) =====
def tsp_backtracking(G, inicio):
    nodos = list(G.nodes)
    nodos.remove(inicio)
    min_ruta = None
    min_distancia = float('inf')

    for perm in itertools.permutations(nodos):
        ruta = [inicio] + list(perm) + [inicio]
        distancia = sum(G[ruta[i]][ruta[i+1]]['weight'] for i in range(len(ruta)-1))
        if distancia < min_distancia:
            min_distancia = distancia
            min_ruta = ruta

    return min_ruta, min_distancia

# ===== 4. VISUALIZACIÓN =====
def mostrar_grafo(G, ruta=None, titulo="Red de Ciudades"):
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if ruta:
        path_edges = list(zip(ruta, ruta[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title(titulo)
    plt.show()

# ===== 5. INTERFAZ DE USUARIO =====
def menu():
    print("=== OPTIMIZADOR DE RUTAS DE ENTREGA ===")
    n = int(input("¿Cuántas ciudades quieres? (<=8 para backtracking): "))
    ciudades = [f"C{i}" for i in range(n)]
    G = crear_grafo(ciudades)

    while True:
        print("\n--- Menú ---")
        print("1. Mostrar red de ciudades")
        print("2. Resolver con Nearest Neighbor")
        print("3. Resolver con Backtracking")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_grafo(G)
        elif opcion == "2":
            inicio = input(f"Ciudad inicial ({', '.join(ciudades)}): ")
            if inicio not in ciudades:
                print("Ciudad no válida.")
                continue
            ruta, dist = nearest_neighbor(G, inicio)
            print(f"Ruta (voraz): {' → '.join(ruta)} | Distancia total: {dist}")
            mostrar_grafo(G, ruta, "Ruta Voraz")
        elif opcion == "3":
            if n > 8:
                print("Backtracking es muy lento para más de 8 ciudades.")
                continue
            inicio = input(f"Ciudad inicial ({', '.join(ciudades)}): ")
            if inicio not in ciudades:
                print("Ciudad no válida.")
                continue
            ruta, dist = tsp_backtracking(G, inicio)
            print(f"Ruta (óptima): {' → '.join(ruta)} | Distancia total: {dist}")
            mostrar_grafo(G, ruta, "Ruta Óptima (Backtracking)")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# ===== EJECUCIÓN PRINCIPAL =====
if __name__ == "__main__":
    menu()

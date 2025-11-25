# busqueda.py

from base_conocimiento import CONEXIONES
import heapq  # para la cola de prioridad (Dijkstra)


def construir_grafo():
    """
    Construye un grafo como diccionario de adyacencias a partir de CONEXIONES.
    """
    grafo = {}

    for c in CONEXIONES:
        o = c["origen"]
        d = c["destino"]
        t = c["tiempo"]

        # Conexión origen -> destino
        grafo.setdefault(o, []).append((d, t))
        # Conexión destino -> origen (para poder viajar en ambos sentidos)
        grafo.setdefault(d, []).append((o, t))

    return grafo


def dijkstra(inicio, fin):
    """
    Encuentra la ruta de menor costo usando Dijkstra.
    Devuelve (costo_total, ruta).
    """
    grafo = construir_grafo()

    # (costo_acumulado, nodo_actual, ruta_hasta_ahora)
    cola = [(0, inicio, [inicio])]
    visitados = set()

    while cola:
        costo, nodo, ruta = heapq.heappop(cola)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        # Si llegamos al destino, devolvemos
        if nodo == fin:
            return costo, ruta

        # Revisar vecinos
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitados:
                nuevo_costo = costo + peso
                nueva_ruta = ruta + [vecino]
                heapq.heappush(cola, (nuevo_costo, vecino, nueva_ruta))

    # Si no hay ruta
    return None, []

# busqueda.py
import heapq
from base_conocimiento import CONEXIONES


def construir_grafo():
    """
    Convierte la lista de CONEXIONES en un grafo:
    { estación: [(vecino, tiempo), ...], ... }
    """
    grafo = {}

    for c in CONEXIONES:
        origen = c["origen"]
        destino = c["destino"]
        tiempo = c["tiempo"]

        # Como TransMilenio va en ambos sentidos, conectamos las dos formas
        grafo.setdefault(origen, []).append((destino, tiempo))
        grafo.setdefault(destino, []).append((origen, tiempo))

    return grafo


def dijkstra(origen, destino):
    grafo = construir_grafo()

    # Por seguridad: si alguna estación no existe en el grafo
    if origen not in grafo or destino not in grafo:
        return float("inf"), []

    # Inicializar distancias
    dist = {nodo: float("inf") for nodo in grafo}
    previo = {nodo: None for nodo in grafo}
    dist[origen] = 0

    # Cola de prioridad (costo, nodo)
    pq = [(0, origen)]

    while pq:
        costo_actual, nodo = heapq.heappop(pq)

        # Si ya tenemos el mejor costo conocido a este nodo, seguimos
        if costo_actual > dist[nodo]:
            continue

        # Si llegamos al destino, podemos cortar
        if nodo == destino:
            break

        for vecino, peso in grafo[nodo]:
            nuevo_costo = costo_actual + peso
            if nuevo_costo < dist[vecino]:
                dist[vecino] = nuevo_costo
                previo[vecino] = nodo
                heapq.heappush(pq, (nuevo_costo, vecino))

    # Si no hay camino
    if dist[destino] == float("inf"):
        return float("inf"), []

    # Reconstruir ruta desde el destino hasta el origen
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = previo[actual]

    ruta.reverse()
    return dist[destino], ruta

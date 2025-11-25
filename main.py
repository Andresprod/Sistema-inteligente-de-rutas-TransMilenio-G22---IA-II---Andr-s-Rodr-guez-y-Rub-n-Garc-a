from busqueda import dijkstra
from base_conocimiento import CONEXIONES

def listar_estaciones():
    estaciones = set()
    for c in CONEXIONES:
        estaciones.add(c["origen"])
        estaciones.add(c["destino"])
    return sorted(estaciones)

def main():
    print("=== Sistema inteligente de rutas - TransMilenio G22 ===\n")
    print("Estaciones disponibles:")
    for est in listar_estaciones():
        print(" -", est)

    origen = input("\nIngrese estación de origen (copie el nombre tal cual): ").strip()
    destino = input("Ingrese estación de destino (copie el nombre tal cual): ").strip()

    costo, ruta = dijkstra(origen, destino)

    if ruta:
        print("\nMejor ruta encontrada:")
        print(" -> ".join(ruta))
        print(f"Tiempo total estimado del viaje: {costo} minutos")
        print(f"Número total de estaciones en la ruta: {len(ruta)}")
    else:
        print("\nNo se encontró ruta entre esas estaciones.")

if __name__ == "__main__":
    main()

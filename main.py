# main.py
from base_conocimiento import CONEXIONES
from busqueda import dijkstra


def obtener_estaciones():
    """Devuelve un conjunto con todas las estaciones conocidas."""
    estaciones = set()
    for c in CONEXIONES:
        estaciones.add(c["origen"])
        estaciones.add(c["destino"])
    return estaciones


def mostrar_estaciones_disponibles(estaciones):
    print("\nEstaciones disponibles:")
    for nombre in sorted(estaciones):
        print(f" - {nombre}")


def main():
    estaciones = obtener_estaciones()

    print("=== Sistema inteligente de rutas – TransMilenio G22 ===")
    mostrar_estaciones_disponibles(estaciones)
    print()

    origen = input("Ingrese estación de origen (escriba exactamente el nombre): ").strip()
    destino = input("Ingrese estación de destino (escriba exactamente el nombre): ").strip()

    # 🛑 Validación 1: ¿existe la estación de origen?
    if origen not in estaciones:
        print(f"\n❌ Error: la estación '{origen}' no existe en la base de datos.")
        mostrar_estaciones_disponibles(estaciones)
        return

    # 🛑 Validación 2: ¿existe la estación de destino?
    if destino not in estaciones:
        print(f"\n❌ Error: la estación '{destino}' no existe en la base de datos.")
        mostrar_estaciones_disponibles(estaciones)
        return

    # ✅ Si todo está bien, ahora sí buscamos la mejor ruta
    costo, ruta = dijkstra(origen, destino)

    if ruta:
        print("\n✅ Mejor ruta encontrada:")
        print(" -> ".join(ruta))
        print(f"⏱  Tiempo total estimado del viaje: {costo} minutos")
        print(f"🚏  Número total de estaciones en la ruta: {len(ruta)}")
    else:
        print("\n⚠ No se encontró ruta entre esas estaciones (aunque ambas existen en la base de datos).")


if __name__ == "__main__":
    main()

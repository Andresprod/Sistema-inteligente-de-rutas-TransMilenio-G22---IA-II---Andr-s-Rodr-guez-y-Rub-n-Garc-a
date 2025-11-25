from base_conocimiento import CONEXIONES
from busqueda import dijkstra


def obtener_estaciones():
    """Devuelve un conjunto con todas las estaciones del sistema."""
    estaciones = set()
    for c in CONEXIONES:
        estaciones.add(c["origen"])
        estaciones.add(c["destino"])
    return estaciones


def mostrar_estaciones(estaciones):
    print("\nEstaciones disponibles:")
    for est in sorted(estaciones):
        print(" -", est)


def pedir_estacion(mensaje, estaciones):
    """Repite hasta que el usuario escriba una estación válida."""
    while True:
        est = input(mensaje).strip()
        if est in estaciones:
            return est
        print(f"\n❌ Error: la estación '{est}' no existe.")
        print("Por favor escriba una estación válida como aparece en la lista:\n")
        mostrar_estaciones(estaciones)


def main():
    estaciones = obtener_estaciones()

    print("\n=== Sistema inteligente de rutas – TransMilenio G22 ===\n")
    mostrar_estaciones(estaciones)

    # ⬇️ AQUÍ PEDIMOS ORIGEN Y DESTINO
    while True:
        origen = pedir_estacion("\nIngrese estación de ORIGEN: ", estaciones)
        destino = pedir_estacion("Ingrese estación de DESTINO: ", estaciones)

        # 🛑 NUEVO CONDICIONAL: ORIGEN = DESTINO
        if origen == destino:
            print("\n❌ Error: la estación de ORIGEN y DESTINO no pueden ser la misma.")
            print("Por favor verifique la información e intente nuevamente.")
            continue  # 🔄 vuelve a pedir las estaciones

        # Si llegamos aquí, las estaciones son válidas y diferentes
        break

    # Ejecutar búsqueda SOLO cuando todo está correcto
    costo, ruta = dijkstra(origen, destino)

    if ruta:
        print("\n✅ Mejor ruta encontrada:")
        print(" -> ".join(ruta))
        print(f"\n⏱  Tiempo estimado: {costo} minutos")
        print(f"🚏  Número de estaciones: {len(ruta)}")
    else:
        print("\n⚠ No hay ruta disponible entre esas estaciones.")


if __name__ == "__main__":
    main()

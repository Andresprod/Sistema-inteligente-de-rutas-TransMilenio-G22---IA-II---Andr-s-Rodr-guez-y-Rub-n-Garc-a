from base_conocimiento import CONEXIONES
from busqueda import dijkstra
import joblib
import os
import pandas as pd


# ===============================
# UTILIDADES DE ESTACIONES
# ===============================

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


def pedir_hora():
    """Pide una hora válida entre 0 y 23."""
    while True:
        try:
            hora = int(input("\nIngrese la HORA del viaje (0-23): "))
            if 0 <= hora <= 23:
                return hora
            else:
                print("❌ La hora debe estar entre 0 y 23.")
        except ValueError:
            print("❌ Debe ingresar un número entero.")


# ===============================
# MODELO ML
# ===============================

def cargar_modelo_si_existe():
    ruta = "dataset/modelo_entrenado.pkl"
    if os.path.exists(ruta):
        modelo = joblib.load(ruta)
        return modelo, ruta
    return None, None


# ===============================
# MAIN
# ===============================

def main():
    estaciones = obtener_estaciones()

    print("\n=== Sistema inteligente de rutas – TransMilenio G22 ===\n")
    mostrar_estaciones(estaciones)

    # Pedir ORIGEN y DESTINO válidos y diferentes
    while True:
        origen = pedir_estacion("\nIngrese estación de ORIGEN: ", estaciones)
        destino = pedir_estacion("Ingrese estación de DESTINO: ", estaciones)

        if origen == destino:
            print("\n❌ Error: ORIGEN y DESTINO no pueden ser la misma estación.")
            print("Intente nuevamente.\n")
            continue
        break

    # Pedir hora
    hora = pedir_hora()

    # ===============================
    # 1) BÚSQUEDA CLÁSICA (DIJKSTRA)
    # ===============================
    costo, ruta = dijkstra(origen, destino)

    if ruta:
        print("\n✅ Mejor ruta encontrada (Dijkstra):")
        print(" -> ".join(ruta))
        print(f"\n⏱ Tiempo estimado (Dijkstra): {costo} minutos")
        print(f"🚏 Número de estaciones en la ruta: {len(ruta)}")

        # ===============================
        # 2) PREDICCIÓN CON ML
        # ===============================
        modelo, ruta_modelo = cargar_modelo_si_existe()

        if modelo is None:
            print("\n⚠️ Modelo ML no encontrado.")
            print("Entrena el modelo ejecutando: python dataset/modelo_ml.py")
        else:
            num_estaciones = len(ruta)

            # 👇 AQUÍ ESTÁ LA CORRECCIÓN CLAVE (DataFrame con nombres de columnas)
            X_pred = pd.DataFrame([{
                "num_estaciones": num_estaciones,
                "hora": hora
            }])

            try:
                pred = modelo.predict(X_pred)[0]
                print("\n🤖 Predicción del modelo ML:")
                print(f"📦 Modelo cargado desde: {ruta_modelo}")
                print(f"⏱ Tiempo estimado (ML): {pred:.2f} minutos")
            except Exception as e:
                print("\n⚠️ Error al calcular la predicción ML.")
                print(f"Detalle: {e}")

    else:
        print("\n⚠ No hay ruta disponible entre esas estaciones.")


# ===============================
# EJECUCIÓN
# ===============================

if __name__ == "__main__":
    main()

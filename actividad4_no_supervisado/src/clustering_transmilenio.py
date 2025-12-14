# clustering_transmilenio.py
# Aprendizaje NO supervisado – Clustering de rutas TransMilenio

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def cargar_datos():
    """
    Carga el dataset para clustering
    """
    return pd.read_csv(
        "actividad4_no_supervisado/dataset/rutas_transmilenio_cluster.csv"
    )


def entrenar_clustering(X, k=3):
    """
    Entrena el modelo K-Means
    """
    modelo = KMeans(n_clusters=k, random_state=42, n_init=10)
    modelo.fit(X)
    return modelo


def main():
    print("\n=== Clustering de rutas TransMilenio ===\n")

    # 1️⃣ Cargar datos
    data = cargar_datos()

    # 2️⃣ Seleccionar variables numéricas para clustering
    X = data[["hora", "congestion", "num_estaciones", "tiempo_total_min"]]

    # 3️⃣ Escalar datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 4️⃣ Entrenar modelo de clustering
    modelo = entrenar_clustering(X_scaled, k=3)

    # 5️⃣ Asignar cluster a cada ruta
    data["cluster"] = modelo.labels_

    # 6️⃣ Nombres semánticos de los clusters
    nombres_clusters = {
        0: "Rutas cortas y baja congestión",
        1: "Rutas medias con congestión moderada",
        2: "Rutas largas y alta congestión"
    }

    print("Clustering realizado correctamente\n")
    print("Cantidad de rutas por tipo de cluster:\n")

    conteo = data["cluster"].value_counts()

    for cluster_id, cantidad in conteo.items():
        descripcion = nombres_clusters.get(
            cluster_id, "Cluster no identificado"
        )
        print(f"- {descripcion}: {cantidad} rutas")

    # 7️⃣ Guardar resultados
    output_path = (
        "actividad4_no_supervisado/results/rutas_clusterizadas.csv"
    )
    data.to_csv(output_path, index=False)

    print("\nResultados guardados en:")
    print(output_path)


if __name__ == "__main__":
    main()

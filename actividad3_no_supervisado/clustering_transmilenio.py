# clustering_transmilenio.py
# Aprendizaje NO supervisado - Clustering de rutas TransMilenio

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def cargar_datos():
    """
    Carga el dataset para clustering
    """
    return pd.read_csv("actividad3_no_supervisado/dataset/rutas_transmilenio_cluster.csv")


def preparar_datos(data):
    """
    Selecciona variables numéricas y las escala
    """
    X = data[["num_estaciones", "hora", "congestion"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled


def entrenar_clustering(X_scaled, k=3):
    """
    Entrena el modelo KMeans
    """
    modelo = KMeans(n_clusters=k, random_state=42)
    modelo.fit(X_scaled)

    return modelo


def main():
    print("\n=== Clustering de rutas TransMilenio ===\n")

    data = cargar_datos()
    X_scaled = preparar_datos(data)

    modelo = entrenar_clustering(X_scaled, k=3)

    data["cluster"] = modelo.labels_

    print("Clustering realizado correctamente\n")
    print("Cantidad de rutas por cluster:")
    print(data["cluster"].value_counts())

    data.to_csv(
        "actividad3_no_supervisado/results/rutas_clusterizadas.csv",
        index=False
    )

    print("\nResultados guardados en:")
    print("actividad3_no_supervisado/results/rutas_clusterizadas.csv")


if __name__ == "__main__":
    main()

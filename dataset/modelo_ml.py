# modelo_ml.py
# Modelo de aprendizaje supervisado para estimar tiempo de viaje

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

def cargar_datos():
    """
    Carga el dataset de rutas de TransMilenio
    """
    return pd.read_csv("dataset/rutas_transmilenio.csv")


def entrenar_modelo():
    """
    Entrena un árbol de decisión para predecir tiempo de viaje
    """
    data = cargar_datos()

    # Variables de entrada (features)
    X = data[["num_estaciones", "hora"]]

    # Variable objetivo
    y = data["tiempo_total_min"]

    # Separar datos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Crear y entrenar el modelo
    modelo = DecisionTreeRegressor(random_state=42)
    modelo.fit(X_train, y_train)

    # Evaluar el modelo
    predicciones = modelo.predict(X_test)
    error = mean_absolute_error(y_test, predicciones)

    print("Modelo entrenado correctamente")
    print(f"Error promedio del modelo: {error:.2f} minutos")
    

    joblib.dump(modelo, "dataset/modelo_entrenado.pkl")
    print("Modelo guardado en dataset/modelo_entrenado.pkl")

    return modelo


if __name__ == "__main__":
    entrenar_modelo()

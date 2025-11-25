# base_conocimiento.py

# tiempo = minutos ficticios entre estaciones (entre 5 y 15)

CONEXIONES = [
    {"origen": "Portal 80", "destino": "Granja - Carrera 77", "linea": "G22", "tiempo": 7},
    {"origen": "Granja - Carrera 77", "destino": "Minuto de Dios", "linea": "G22", "tiempo": 6},
    {"origen": "Minuto de Dios", "destino": "Boyacá", "linea": "G22", "tiempo": 8},
    {"origen": "Boyacá", "destino": "Avenida 68", "linea": "G22", "tiempo": 5},
    {"origen": "Avenida 68", "destino": "Carrera 47", "linea": "G22", "tiempo": 9},
    {"origen": "Carrera 47", "destino": "NQS Calle 75", "linea": "G22", "tiempo": 10},
    {"origen": "NQS Calle 75", "destino": "AV. Chile", "linea": "G22", "tiempo": 6},
    {"origen": "AV. Chile", "destino": "U. Nacional", "linea": "G22", "tiempo": 7},
    {"origen": "U. Nacional", "destino": "AV. El Dorado", "linea": "G22", "tiempo": 5},
    {"origen": "AV. El Dorado", "destino": "Paloquemao", "linea": "G22", "tiempo": 12},
    {"origen": "Paloquemao", "destino": "Santa Isabel", "linea": "G22", "tiempo": 8},
    {"origen": "Santa Isabel", "destino": "General Santander", "linea": "G22", "tiempo": 9},
    {"origen": "General Santander", "destino": "Sevillana", "linea": "G22", "tiempo": 11},
    {"origen": "Sevillana", "destino": "Portal Sur - JFK Coop.Financiera", "linea": "G22", "tiempo": 10},
]

def hay_conexion(origen, destino):
    for c in CONEXIONES:
        if c["origen"] == origen and c["destino"] == destino:
            return True
    return False

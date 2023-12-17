import requests
from datetime import datetime

def actualizar_tipo_cambio(database):
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        valor_cambio = data.get('venta', 0.0)  # Ajusta esto según la estructura de la API

        query_insert = f"INSERT INTO tipo_cambio (fecha, valor_cambio) VALUES ('{fecha_actual}', {valor_cambio});"
        database.execute_query(query_insert)
        print("Tipo de cambio actualizado correctamente.")
    else:
        print("Error al obtener el tipo de cambio desde la API.")

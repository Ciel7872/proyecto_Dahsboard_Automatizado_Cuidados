import requests
import pandas as pd
from datetime import datetime

# URL base oficial de la API de CEPALSTAT
CEPAL_BASE_URL = "https://api-cepalstat.cepal.org/cepalstat/api/v1"

# Diccionario de Indicadores clave para el Bloque 3 (Deben verificarse en el catálogo de CEPALSTAT)
INDICADORES_CUIDADO = {
    "feminizacion_pobreza": 3192,  # ID de ejemplo: Índice de feminidad de la pobreza
    "participacion_laboral_mujeres": 3285, # ID de ejemplo: Tasa de participación económica
    "desempleo_mujeres": 3286, # ID de ejemplo: Tasa de desocupación
    "nini_mujeres": 3290 # ID de ejemplo: Jóvenes que no estudian ni trabajan
}

def obtener_dato_cepal(indicator_id, iso_country="ARG"):
    """
    Consulta la API de CEPALSTAT para un indicador específico y un país.
    Devuelve el último valor disponible.
    """
    # Endpoint para obtener los datos del indicador
    url = f"{CEPAL_BASE_URL}/indicator/{indicator_id}/data"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza error si el status no es 200 OK
        data = response.json()
        
        # Filtramos los datos para el país solicitado (ej. "ARG" para Argentina)
        datos_pais = [item for item in data['body']['data'] if item.get('dim_190') == iso_country]
        
        if not datos_pais:
            return {"error": "No hay datos para este país"}
        
        # Ordenamos por año para agarrar el dato más reciente
        datos_pais.sort(key=lambda x: str(x.get('dim_time', '0')), reverse=True)
        ultimo_dato = datos_pais[0]
        
        return {
            "indicador_id": indicator_id,
            "pais": iso_country,
            "anio": ultimo_dato.get('dim_time'),
            "valor": ultimo_dato.get('value'),
            "unidad": data['body']['metadata'].get('unit_of_measure', 'N/A')
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con CEPAL: {e}")
        return None

# --- Pruebas rápidas (Esto luego se borra o se mueve a notebooks/) ---
if __name__ == "__main__":
    print("Testeando conexión a CEPAL para Feminización de la Pobreza...")
    resultado = obtener_dato_cepal(INDICADORES_CUIDADO["feminizacion_pobreza"])
    print(resultado)
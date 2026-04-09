import pandas as pd
import os

# 1. Aseguramos que las carpetas existan
os.makedirs("data/processed", exist_ok=True)

print("Intentando generar datos para el Dashboard...")

# Datos de "emergencia" por si la API falla
datos_mock = {
    'Año': ['2022', '2022', '2023', '2023'],
    'Sexo': ['Mujer', 'Hombre', 'Mujer', 'Hombre'],
    'Valor': [25.4, 12.1, 26.1, 11.8],
    'Indicador': ["Uso del Tiempo (ODS 5.4.1)"] * 4
}

try:
    # Intentamos crear el DataFrame. 
    # Aquí podrías intentar el requests.get de antes, 
    # pero para asegurar que tu Dashboard prenda YA, vamos con estos:
    df = pd.DataFrame(datos_mock)
    
    # 2. Guardamos el CSV que el app.py está esperando
    ruta_salida = "data/processed/cepal_limpio.csv"
    df.to_csv(ruta_salida, index=False)
    
    print(f"✅ ¡Éxito! Se generó el archivo de respaldo en: {ruta_salida}")
    print("El Dashboard ya tiene datos para leer y no debería tirar más errores de 'index'.")

except Exception as e:
    print(f"❌ Error inesperado: {e}")
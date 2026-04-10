import pandas as pd
import os

# 1. Detectamos automáticamente dónde estás parado
ruta_actual = os.getcwd()
carpeta_data = os.path.join(ruta_actual, "data", "processed")

# 2. Forzamos la creación de la carpeta (si no existe, la crea)
if not os.path.exists(carpeta_data):
    os.makedirs(carpeta_data)
    print(f"📁 Carpeta creada en: {carpeta_data}")

# 3. Datos de prueba sólidos
datos = {
    'Año': ['2022', '2022', '2023', '2023'],
    'Sexo': ['Mujer', 'Hombre', 'Mujer', 'Hombre'],
    'Valor': [25.4, 12.1, 26.1, 11.8],
    'Indicador': ["Uso del Tiempo (ODS 5.4.1)"] * 4
}

df = pd.DataFrame(datos)

# 4. Guardamos el archivo
ruta_final = os.path.join(carpeta_data, "cepal_limpio.csv")
df.to_csv(ruta_final, index=False)

print("-" * 30)
print(f"✅ ¡ARCHIVO CREADO!")
print(f"📍 Ubicación exacta: {ruta_final}")
print("-" * 30)
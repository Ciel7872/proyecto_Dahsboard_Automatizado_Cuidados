import requests
import pandas as pd
import streamlit as st

# --- DICCIONARIOS DE TRADUCCIÓN ---
# Usamos strings ("1") porque las APIs suelen mandar los números como texto
MAPEO_SEXO = {"1": "Hombre", "2": "Mujer", "3": "Ambos sexos"}
MAPEO_ZONA = {"1": "Nacional", "2": "Urbana", "3": "Rural"}

class CepalMonitor:
    def __init__(self):
        self.base_url = "https://api-cepalstat.cepal.org/cepalstat/api/v1"
        self.arg_id = 32  # Argentina

    @st.cache_data 
    def fetch_benchmark(_self, indicator_id):
        endpoint = f"{_self.base_url}/indicator/{indicator_id}/data"
        params = {"lang": "es", "format": "json", "members": _self.arg_id}
        try:
            r = requests.get(endpoint, params=params)
            r.raise_for_status()
            
            datos_lista = r.json()['body']['data']
            df = pd.json_normalize(datos_lista)
            
            # --- MAGIA DE DATA ANALYST (Traducción y Limpieza) ---
            # 1. Traducimos los códigos numéricos a palabras
            if 'dim_228' in df.columns:
                df['Sexo'] = df['dim_228'].astype(str).map(MAPEO_SEXO).fillna(df['dim_228'])
            
            if 'dim_229' in df.columns:
                df['Zona'] = df['dim_229'].astype(str).map(MAPEO_ZONA).fillna(df['dim_229'])

            # 2. Renombramos la columna del tiempo
            if 'dim_time' in df.columns:
                df['Año'] = df['dim_time']
                
            # 3. Nos quedamos solo con las columnas limpias
            columnas_finales = [col for col in ['Año', 'Sexo', 'Zona', 'value'] if col in df.columns]
            df = df[columnas_finales]
            
            # 4. Le ponemos un nombre más claro al valor final
            df = df.rename(columns={'value': 'Horas / Porcentaje'})
            # -----------------------------------------------------
            
            return df
        except Exception as e:
            st.error(f"Error al procesar los datos: {e}")
            return None

# --- MAPEO REAL ---
KPI_MAP = {
    "Uso del Tiempo (ODS 5.4.1)": 3201,
    "Feminización de la Pobreza": 3330,
    "Participación Laboral (%)": 2470,
    "Fuera del Mercado por Cuidados": 5531,
    "Jóvenes NINI (15-24 años)": 3469,
    "Dependencia Demográfica": 4792,
    "Hogares Jefatura Femenina": 2465,
    "Asistencia Escolar (6-11 años)": 4977
}

def main():
    st.set_page_config(page_title="Monitor CEPAL", layout="wide")
    st.title("📊 Benchmark Nacional (CEPALSTAT)")
    
    monitor = CepalMonitor()
    
    with st.sidebar:
        st.header("Filtros de API")
        seleccion = st.selectbox("Seleccioná métrica de comparación:", list(KPI_MAP.keys()))
        btn = st.button("Consultar API")

    if btn:
        id_api = KPI_MAP[seleccion]
        df = monitor.fetch_benchmark(id_api) 
        
        if df is not None and not df.empty:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric("Indicador Seleccionado", seleccion)
                st.write(f"ID Técnico: {id_api}")
            with col2:
                st.subheader("Serie Histórica Argentina")
                # Mostramos la tabla ocupando todo el ancho disponible
                st.dataframe(df, use_container_width=True) 
        else:
            st.error("No hay datos disponibles para Argentina en este indicador.")

if __name__ == "__main__":
    main()